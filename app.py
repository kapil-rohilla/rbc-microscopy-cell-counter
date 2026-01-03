import streamlit as st
import cv2
import numpy as np
from cell_counter import final_rbc_counter_image

st.title("RBC Cell Counter")

uploaded = st.file_uploader("Upload RBC Microscopic Image", type=["jpg","jpeg","png"])

if uploaded:
    file_bytes = np.frombuffer(uploaded.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB),
         caption="Uploaded Image",
         use_container_width=True)

    count, overlay = final_rbc_counter_image(img)

    st.subheader(f"Total RBC Count: **{count}**")

    st.image(cv2.cvtColor(overlay, cv2.COLOR_BGR2RGB),
             caption="Detected RBCs",
             use_container_width=True)