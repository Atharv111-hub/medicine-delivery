import streamlit as st

def show_cart():
    st.subheader("Your Cart")
    cart = st.session_state.get("cart", [])
    if not cart:
        st.info("Your cart is empty.")
        return False
    total = 0
    for item in cart:
        st.write(f"- {item['name']} x {item['qty']} = ₹{item['price']*item['qty']}")
        total += item['price'] * item['qty']
    st.write(f"**Total: ₹{total}**")
    return True
