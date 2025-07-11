import json
import os
import base64
from datetime import datetime

# --- File Names ---
USERS_FILE = "users.json"
MEDICINES_FILE = "medicines.json"
ORDERS_FILE = "orders.json"
CONSULTS_FILE = "consultations.json"

# --- Helper functions for JSON ---
def load_json(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return json.load(f)

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def load_user_data():
    if not os.path.exists(USERS_FILE):
        return {}
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except Exception:
        return {}

def save_user_data(user_data):
    with open(USERS_FILE, "w") as file:
        json.dump(user_data, file, indent=2)

# --- Email and Password Validation ---
def is_valid_email(email):
    if "@" not in email or email.count("@") != 1:
        return False
    local_part, domain_part = email.split("@")
    if not local_part or not domain_part:
        return False
    allowed_local_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._%+-")
    if any(char not in allowed_local_chars for char in local_part):
        return False
    if "." not in domain_part:
        return False
    domain_parts = domain_part.split(".")
    if len(domain_parts) < 2:
        return False
    domain_name = domain_parts[0]
    if not domain_name or any(char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-" for char in domain_name):
        return False
    for extension in domain_parts[1:]:
        if len(extension) < 2 or not extension.isalpha():
            return False
    return True

def is_valid_password(password):
    if len(password) < 6:
        return False, "Password must be at least 6 characters."
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-_+="
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
    if not has_uppercase:
        return False, "Password must have at least one uppercase letter."
    if not has_lowercase:
        return False, "Password must have at least one lowercase letter."
    if not has_digit:
        return False, "Password must have at least one digit."
    if not has_special:
        return False, f"Password must have at least one special character: {special_characters}"
    return True, ""

# --- Background image using base64 ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(st, img_path="static/1752061034840.jpg"):
    if os.path.exists(img_path):
        img_base64 = get_base64_of_bin_file(img_path)
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{img_base64}");
                background-attachment: fixed;
                background-size: cover;
                background-position: center;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning(f"Background image not found at {img_path}")

# --- Rerun helper ---
def rerun(st):
    try:
        st.experimental_rerun()
    except AttributeError:
        st.rerun()
