import streamlit as st
from utils import rerun

def login_page():
    st.header("🔐 Login to Your Account")
    st.markdown(
        """
        <style>
        .form-container {
            max-width: 400px;
            margin: auto;
        }
        .error-msg {
            color: #e53e3e;
            font-weight: 600;
            margin-bottom: 10px;
        }
        .success-msg {
            color: #38a169;
            font-weight: 600;
            margin-bottom: 10px;
        }
        </style>
        """, unsafe_allow_html=True
    )

    with st.form("login_form"):
        st.markdown('<div class="form-container">', unsafe_allow_html=True)

        username = st.text_input("Username", max_chars=20)
        
        # Password input with show/hide toggle
        password = st.text_input("Password", type="password", key="login_password")

        login_button = st.form_submit_button("Login")

        st.markdown('</div>', unsafe_allow_html=True)

        if login_button:
            # Validate inputs
            if not username or not password:
                st.warning("⚠️ Please fill in all fields.")
            elif "user_data" not in st.session_state or username not in st.session_state["user_data"]:
                st.error("❌ User not found.")
            elif st.session_state["user_data"][username]["password"] != password:
                st.error("❌ Incorrect password.")
            else:
                with st.spinner("Logging you in..."):
                    # Simulate processing delay if needed
                    import time
                    time.sleep(1)

                st.success(f"✅ Welcome back, **{username}**!")
                st.session_state["is_logged_in"] = True
                st.session_state["current_user"] = username
                st.session_state["current_page"] = "dashboard"
                rerun(st)
