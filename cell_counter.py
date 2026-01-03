import cv2
import numpy as np

def final_rbc_counter_image(img0):

    #Crop microscope circle
    h, w = img0.shape[:2]
    mask = np.zeros((h, w), np.uint8)
    cv2.circle(mask, (w//2, h//2), min(h,w)//2 - 10, 255, -1)
    img = cv2.bitwise_and(img0, img0, mask=mask)

    # Resize
    scale = 900 / max(h, w)
    img = cv2.resize(img, (int(w*scale), int(h*scale)))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8,8))
    gray = clahe.apply(gray)
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    mask1 = cv2.adaptiveThreshold(
        blur, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        41, 5
    )

    if mask1.sum() < 30000:
        _, mask1 = cv2.threshold(
            blur, 0, 255,
            cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
        )

    #Morphological operations
    kernel = np.ones((3,3), np.uint8)

    #remove noise
    opening = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel, iterations=1)

    # Erode (KEY STEP to separate touching RBCs)
    opening = cv2.erode(opening, kernel, iterations=1)

    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    dist = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

    # LOWERED THRESHOLD → MORE MARKERS → Better splitting
    ret, sure_fg = cv2.threshold(dist, 0.28 * dist.max(), 255, 0)

    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    # Marker labeling
    ret, markers = cv2.connectedComponents(sure_fg)
    markers += 1
    markers[unknown == 255] = 0

    img_ws = img.copy()
    cv2.watershed(img_ws, markers)

    #Count RBCs & draw overlay
    count = 0
    overlay = img.copy()

    for label in np.unique(markers):
        if label <= 1:
            continue

        comp = (markers == label).astype('uint8') * 255
        cnts, _ = cv2.findContours(
            comp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        if cnts:
            c = max(cnts, key=cv2.contourArea)
            area = cv2.contourArea(c)

            # RBC area range
            if 50 < area < 5000:
                (x,y), r = cv2.minEnclosingCircle(c)
                cv2.circle(overlay, (int(x),int(y)), int(r), (0,255,0), 1)
                count += 1

    return count, overlay