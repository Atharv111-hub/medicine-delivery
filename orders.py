import streamlit as st
from datetime import datetime
from utils import load_json, save_json, ORDERS_FILE
from cart import show_cart

def place_order(username):
    if not show_cart():
        return
    address = st.text_input("Delivery Address", value=st.session_state.get("address", ""), key="order_address")
    if st.button("Place Order"):
        if not address.strip():
            st.warning("Please enter your delivery address.")
            return
        orders = load_json(ORDERS_FILE)
        order = {
            "user": username,
            "items": st.session_state["cart"],
            "total": sum(item["price"] * item["qty"] for item in st.session_state["cart"]),
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "address": address
        }
        orders.append(order)
        save_json(ORDERS_FILE, orders)
        st.session_state["address"] = address
        st.success("Order placed successfully!")
        st.session_state["cart"] = []
        st.session_state["cart_quantities"] = {}

def view_orders(username):
    orders = load_json(ORDERS_FILE)
    user_orders = [o for o in orders if o["user"] == username]
    st.header("Your Orders")
    if not user_orders:
        st.info("No orders yet.")
        return
    for idx, order in enumerate(user_orders, 1):
        st.write(f"Order {idx}:")
        st.write(f"Date: {order.get('datetime', 'N/A')}")
        st.write(f"Address: {order.get('address', 'N/A')}")
        for item in order["items"]:
            st.write(f"- {item['name']} x {item['qty']} = ₹{item['price']*item['qty']}")
        st.write(f"Total: ₹{order['total']}")
        st.markdown("---")
