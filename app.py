import streamlit as st
import cv2
import numpy as np
import base64
from cell_counter import final_rbc_counter_image

# Page config
st.set_page_config(
    page_title="RBC Microscopy Cell Counter",
    layout="centered"
)

def set_background(image_path):
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>

        /* Import clean medical font */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

        html, body, [class*="css"] {{
            font-family: 'Inter', sans-serif;
        }}

        /* Background with gradient overlay */
        .stApp {{
            background:
              linear-gradient(
                rgba(255,255,255,0.75),
                rgba(255,255,255,0.85)
              ),
              url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* Main card (glassmorphism) */
        .block-container {{
            background: rgba(255, 255, 255, 0.75);
            backdrop-filter: blur(12px);
            padding: 2.5rem;
            border-radius: 18px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.08);
            animation: fadeIn 0.8s ease-in-out;
        }}

        /* Headings */
        h1 {{
            font-weight: 700;
            text-align: center;
            letter-spacing: -0.5px;
        }}

        h3 {{
            font-weight: 600;
        }}

        /* File uploader styling */
        div[data-testid="stFileUploader"] {{
            border: 2px dashed #e57373;
            border-radius: 14px;
            padding: 1.5rem;
            transition: all 0.3s ease;
            background: rgba(255,255,255,0.6);
        }}

        div[data-testid="stFileUploader"]:hover {{
            border-color: #d32f2f;
            background: rgba(255,255,255,0.85);
            transform: scale(1.01);
        }}

        /* Metric styling */
        div[data-testid="metric-container"] {{
            background: linear-gradient(135deg, #ffebee, #ffffff);
            border-radius: 14px;
            padding: 1rem;
            box-shadow: inset 0 0 0 1px rgba(0,0,0,0.05);
            animation: popIn 0.4s ease-in-out;
        }}

        /* Images */
        img {{
            border-radius: 12px;
        }}

        /* Animations */
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        @keyframes popIn {{
            from {{ transform: scale(0.95); opacity: 0; }}
            to {{ transform: scale(1); opacity: 1; }}
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


set_background("background.png") 

# Header
st.markdown(
    """
    <h1> RBC Microscopy Cell Counter</h1>
    <p style="text-align:center; font-size:16px; color:#555;">
    Classical computer vision based red blood cell counting
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# File upload
uploaded = st.file_uploader(
    "Upload RBC Microscopic Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded:
    file_bytes = np.frombuffer(uploaded.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("Uploaded Image")
        st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB),
                 use_container_width=True)

    with col2:
        st.subheader("Detection Result")

        with st.spinner("Analyzing and counting RBCs…"):
            count, overlay = final_rbc_counter_image(img)

        st.metric("Total RBC Count", count)

        st.image(cv2.cvtColor(overlay, cv2.COLOR_BGR2RGB),
                 caption="Detected RBCs",
                 use_container_width=True)
# Footer
st.markdown(
    """
    <hr>
    <p style="text-align:center; font-size:13px; color:#666;">
    For educational and research purposes only. Not for medical use.
    </p>
    """,
    unsafe_allow_html=True
)
