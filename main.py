import streamlit as st
from utils import set_background, load_user_data
from landing import landing_page
from signup import signup_page
from login import login_page
from dashboard import welcome_page, rerun

def initialize_session():
    if "user_data" not in st.session_state:
        st.session_state["user_data"] = load_user_data()
    if "is_logged_in" not in st.session_state:
        st.session_state["is_logged_in"] = False
    if "current_user" not in st.session_state:
        st.session_state["current_user"] = ""
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "landing"
    if "cart" not in st.session_state:
        st.session_state["cart"] = []
    if "address" not in st.session_state:
        st.session_state["address"] = ""
    if "cart_quantities" not in st.session_state:
        st.session_state["cart_quantities"] = {}

def main():
    set_background(st)
    initialize_session()
    page = st.session_state.get("current_page", "landing")
    logged_in = st.session_state.get("is_logged_in", False)
    if logged_in:
        welcome_page()
    else:
        if page == "landing":
            landing_page()
        elif page == "login":
            login_page()
            st.info("Don't have an account? Sign Up below 👇")
            if st.button("Go to Sign Up"):
                st.session_state["current_page"] = "signup"
                rerun(st)
        elif page == "signup":
            signup_page()
            st.info("Already have an account? Login below 🔑")
            if st.button("Go to Login"):
                st.session_state["current_page"] = "login"
                rerun(st)
        else:
            st.session_state["current_page"] = "landing"
            landing_page()

if __name__ == "__main__":
    main()
