<h1 align="center">RBC Microscopy Cell Counter</h1>

<p align="center">
<strong>Automated Red Blood Cell Counting from Microscopy Images</strong>
</p>

<p align="center">
A classical computer vision system for detecting and counting red blood cells (RBCs) in microscopic blood smear images
</p>

---

## Overview

**RBC Microscopy Cell Counter** is a computer vision–based application that analyzes **microscopic blood smear images** to automatically:

- Detect individual red blood cells (RBCs)
- Count the total number of RBCs present in an image

The project focuses strictly on **cell detection and counting**, using **classical image processing techniques** such as thresholding, morphological operations, and watershed segmentation.

**No disease detection, diagnosis, or medical inference is performed.**

---

## Demo

![RBC Cell Counter Demo](https://github.com/user-attachments/assets/09bfd474-af27-434b-b6bf-6c574ec6e34d)

---

## Key Features

- Upload microscopy images (`.jpg`, `.jpeg`, `.png`)
- Automatic cropping of the microscope field of view
- Contrast enhancement using **CLAHE**
- Robust RBC segmentation using thresholding + morphology
- Separation of touching cells using **distance transform + watershed**
- Geometric filtering to remove noise and artifacts
- Accurate RBC counting
- Visual overlays highlighting detected cells
- Interactive **Streamlit** web interface

---

## System Pipeline

1. **Image Upload**
   - User uploads a microscopy image through the Streamlit UI

2. **Preprocessing**
   - Image resizing for consistent scale
   - Grayscale conversion
   - Contrast enhancement using CLAHE
   - Noise reduction with Gaussian blur

3. **RBC Segmentation**
   - Adaptive / Otsu thresholding
   - Morphological opening and erosion
   - Distance transform for separating touching cells
   - Watershed algorithm for precise cell boundaries

4. **Counting & Visualization**
   - Region filtering based on area and shape
   - Final RBC count
   - Circular overlays drawn on detected cells

---

## Project Structure

```text
rbc-microscopy-cell-counter/
│
├── app.py              # Streamlit application
├── cell_counter.py     # RBC detection & counting logic
├── requirements.txt    # Python dependencies
└── README.md
```
---
## Installation
1) Clone the repository
```bash
git clone https://github.com/kapil-rohilla/rbc-microscopy-cell-counter.git
cd rbc-microscopy-cell-counter
```

2) Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

3) Install dependencies
```bash
pip install -r requirements.txt
```

4) Running the Application
```bash
streamlit run app.py
```

---

## Dependencies

- streamlit
- opencv-python-headless
- numpy

---

## Limitations

- Accuracy depends on image quality and staining consistency
- Overlapping or clustered RBCs may reduce counting accuracy
- Designed for controlled microscopy images only
- Not suitable for clinical or diagnostic use
