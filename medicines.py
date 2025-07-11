import streamlit as st
from datetime import datetime
from utils import load_json, MEDICINES_FILE

def show_medicines():
    medicines = load_json(MEDICINES_FILE)
    st.header("Available Medicines")
    if not medicines:
        st.warning("No medicines found. Please ensure 'medicines.json' exists and has valid data.")
        return
    today = datetime.today().date()
    def not_expired(med):
        try:
            if "expiry_date" not in med:
                return True
            return datetime.strptime(med["expiry_date"], "%Y-%m-%d").date() >= today
        except Exception as e:
            st.warning(f"Error parsing expiry date for {med.get('name', '')}: {e}")
            return False
    medicines = [med for med in medicines if not_expired(med)]
    categories = list(sorted(set([med.get("category", "Other") for med in medicines])))
    search = st.text_input("Search by name", key="med_search")
    cat_filter = st.selectbox("Filter by Category", ["All"] + categories, key="med_category")
    only_in_stock = st.checkbox("Show only in-stock medicines", value=True, key="med_stock")
    filtered = []
    for med in medicines:
        if search and search.lower() not in med.get("name", "").lower():
            continue
        if cat_filter != "All" and med.get("category", "Other") != cat_filter:
            continue
        if only_in_stock and med.get("stock", 0) <= 0:
            continue
        filtered.append(med)
    if not filtered:
        st.info("No medicines match your search/filter.")
        return
    for med in filtered:
        key = f"qty_{med.get('id', med.get('name', 'unknown'))}"
        default_qty = st.session_state["cart_quantities"].get(key, 0)
        qty = st.number_input(
            f"Qty ({med.get('name', 'Unknown')})", min_value=0, max_value=med.get('stock', 0), value=default_qty, key=key
        )
        st.session_state["cart_quantities"][key] = qty
    if st.button("Add to Cart"):
        cart = []
        for med in filtered:
            key = f"qty_{med.get('id', med.get('name', 'unknown'))}"
            qty = st.session_state["cart_quantities"].get(key, 0)
            if qty > 0:
                cart.append({
                    "id": med.get("id", ""),
                    "name": med.get("name", ""),
                    "price": med.get("price", 0),
                    "qty": qty
                })
        if cart:
            st.session_state["cart"] = cart
            st.success("Added to cart!")
        else:
            st.warning("Select at least one medicine.")
