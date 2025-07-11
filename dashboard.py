import streamlit as st
from utils import rerun
from medicines import show_medicines
from orders import place_order, view_orders
from consult import consult_doctor, view_consultations

def top_bar():
    col1, col2, col3 = st.columns([1, 6, 1])
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3081/3081559.png", width=50)
    with col2:
        st.markdown("<h2 style='text-align:center; margin: 0;'>Medicine Delivery</h2>", unsafe_allow_html=True)
    with col3:
        cart = st.session_state.get("cart", [])
        cart_count = sum(item["qty"] for item in cart) if cart else 0
        if st.button(f"🛒 Cart ({cart_count})"):
            st.session_state["current_page"] = "Cart & Place Order"
            rerun(st)

def welcome_page():
    top_bar()
    st.title("Medicine Delivery Dashboard")
    menu = st.sidebar.selectbox(
        "Menu",
        [
            "Show Medicines",
            "Cart & Place Order",
            "Order History",
            "Consult a Doctor",
            "Consultation History"
        ]
    )
    username = st.session_state.get("current_user", "unknown")
    if menu == "Show Medicines":
        show_medicines()
    elif menu == "Cart & Place Order":
        place_order(username)
    elif menu == "Order History":
        view_orders(username)
    elif menu == "Consult a Doctor":
        consult_doctor(username)
    elif menu == "Consultation History":
        view_consultations(username)
    if st.sidebar.button("Logout"):
        st.session_state["is_logged_in"] = False
        st.session_state["current_user"] = ""
        st.session_state["cart"] = []
        st.session_state["cart_quantities"] = {}
        st.session_state["current_page"] = "landing"
        rerun(st)
