<h1 align="center">RBC Microscopy Cell Counter</h1>

<p align="center"><strong>Automated Red Blood Cell Counting from Microscopy Images</strong></p>

<p align="center">
Classical computer vision system for detecting and counting red blood cells in microscopic blood smear images
</p>

---

## Overview

**RBC Microscopy Cell Counter** is a computer vision–based application designed to analyze **microscopic blood smear images** and automatically:

- detect individual red blood cells (RBCs)
- count the total number of RBCs present in an image

The project focuses purely on **cell detection and counting**, using **classical image processing techniques** such as thresholding, morphological operations, and watershed segmentation.

No disease detection, classification, or medical inference is performed.

---

## What This Project Does

- Accepts microscopy images (`.jpg`, `.jpeg`, `.png`)
- Automatically crops the microscope field of view
- Enhances contrast using CLAHE
- Segments RBCs using adaptive thresholding
- Separates touching cells using distance transform + watershed
- Counts valid RBCs based on geometric filtering
- Visualizes detected RBCs with overlays
- Provides an interactive Streamlit interface

---

## System Pipeline

1. **Image Upload**
   - User uploads a microscopy image via Streamlit UI

2. **Preprocessing**
   - Resize for consistent scale
   - Convert to grayscale
   - Contrast enhancement (CLAHE)
   - Noise reduction (Gaussian blur)

3. **RBC Segmentation**
   - Adaptive / Otsu thresholding
   - Morphological opening and erosion
   - Distance transform for cell separation
   - Watershed algorithm to split touching cells

4. **Counting & Visualization**
   - Filter detected regions by area
   - Count valid RBCs
   - Draw circular overlays on detected cells

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
