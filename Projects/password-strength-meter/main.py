import streamlit as st
import re
import random
import string

WEAK_PASSWORDS = {"password123", "123456", "qwerty", "welcome", "admin", "passw0rd", "123456789"}

def check_password_strength(password):
    score = 0
    suggestions = []

    if password in WEAK_PASSWORDS:
        return 0, ["⚠️ This password is commonly used and unsafe. Please choose a stronger one."]

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("❌ Password must be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]",password):
        score += 1
    else:
        suggestions.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d",password):
        score += 1
    else:
        suggestions.append("❌ Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]",password):
        score += 1
    else:
        suggestions.append("❌ Include at least one special character (!@#$%^&*).")
    
    return score, suggestions

def generate_password(length = 12):
    characters = string.ascii_letters + string.digits + "!#$%^&*()_+"
    return "".join(random.choice(characters) for _ in range(length))

st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="wide")

st.title("🔐 Password Strength Meter & Generator")
st.write("Assess the strength of your password or generate a secure one!")

option = st.radio("Choose an option",("Check Password Strength", "Generate Strong Password"))

if option == "Check Password Strength":
    password = st.text_input("Enter your password:", type="password")
    if st.button("Analyze Password", use_container_width=True):
        if password:
            score, suggestions = check_password_strength(password)
            if score == 4:
                st.success("✅ Excellent! Your password is strong.")
            elif score == 3:
                st.warning("⚠️ Your password is moderate. Consider improving it.")
            else:
                st.error("❌ Your password is weak. Use the suggestions below to make it stronger.")
            
            for tip in suggestions:
                st.write("- " + tip)

elif option == "Generate Strong Password":
    length = st.slider("Select Password Length", 8, 20,12)
    if st.button("Generate Password", use_container_width=True):
        strong_password = generate_password(length)
        st.success(f"🔑 Your Secure Password: `{strong_password}`")

st.markdown(
    "<h1 style='text-align:center'>Developed By Ibad Ur Rehman</h1>",
    unsafe_allow_html=True
)