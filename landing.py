import streamlit as st
from utils import rerun
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def landing_page():
    st.set_page_config(
        page_title="Medicine Delivery",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # Encode the local image to base64
    img_path = "1752060596527.jpg"  # Change to your image filename
    img_base64 = get_base64_of_bin_file(img_path)

    st.markdown(f"""
    <style>
    /* Hide default Streamlit header and menu */
    header, #MainMenu, footer {{
        visibility: hidden;
        height: 0;
        padding: 0;
        margin: 0;
    }}

    /* Set background image for the entire app */
    .stApp {{
        background-image: url("data:image/jpg;base64,{img_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}

    /* Custom fixed header bar */
    .custom-header {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 48px;
        background-color: #319795;  /* teal color */
        color: white;
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        font-size: 1.25rem;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 9999;
        box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        user-select: none;
    }}

    /* Push page content down so it is not hidden behind header */
    .main > div:first-child {{
        padding-top: 60px !important;
    }}
    </style>

    <div class="custom-header">
        Medicine Delivery - Fast & Reliable Online Pharmacy
    </div>
    """, unsafe_allow_html=True)

    # Your existing page content inside .main container
    st.markdown('<div class="main">', unsafe_allow_html=True)

    st.markdown('<h1 style="text-align:center; color:#2c7a7b; margin-bottom:0.2rem;">Welcome to Medicine Delivery</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-size:1.3rem; color:#4a5568; margin-top:0;">Order medicines & consult doctors online — fast, safe, and reliable.</p>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; font-size:3rem; margin:1.5rem 0;">💊 🚚 🩺</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="display:flex; justify-content:center; gap:2rem; flex-wrap:wrap; margin-bottom:3rem;">
        <div style="background:#e6fffa; border-radius:1rem; padding:1.5rem 2rem; min-width:180px; text-align:center; box-shadow:0 4px 12px rgba(44, 62, 80, 0.1);">
            <div style="font-size:2.4rem; margin-bottom:0.7rem; color:#319795;">🛒</div>
            <strong>Easy Medicine Ordering</strong>
        </div>
        <div style="background:#e6fffa; border-radius:1rem; padding:1.5rem 2rem; min-width:180px; text-align:center; box-shadow:0 4px 12px rgba(44, 62, 80, 0.1);">
            <div style="font-size:2.4rem; margin-bottom:0.7rem; color:#319795;">👩‍⚕️</div>
            <strong>Expert Doctor Consults</strong>
        </div>
        <div style="background:#e6fffa; border-radius:1rem; padding:1.5rem 2rem; min-width:180px; text-align:center; box-shadow:0 4px 12px rgba(44, 62, 80, 0.1);">
            <div style="font-size:2.4rem; margin-bottom:0.7rem; color:#319795;">⚡</div>
            <strong>Fast & Secure Delivery</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🚀 Start", key="start_button", help="Click to start", use_container_width=True):
        st.session_state["current_page"] = "login"
        rerun(st)

    st.markdown(
        '<div style="text-align:center; color:#718096; font-size:0.95rem; margin-top:3.5rem;">'
        'Need help? <a href="mailto:support@meddelivery.com" style="color:#319795; text-decoration:none;">Contact Support</a>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

# Example usage:
# landing_page()
