import streamlit as st
st.set_page_config(page_title="Unit Convertor", layout="centered")

conversions = {
    "Length": {  
        "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371,
        "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701
    },
    "Weight": {
        "Kilogram": 1, "Gram": 1000, "Milligram": 1000000, "Pound": 2.20462, "Ounce": 35.274
    },
    "Temperature": {
        "Celsius": lambda x: x, 
        "Fahrenheit": lambda x: (x * 9/5) + 32, 
        "Kelvin": lambda x: x + 273.15
    }
}

def convert_units(value, unit_from, unit_to,category):
    if category == "Temperature":
        if unit_from == "Celsius":
            temp = value
        elif unit_from == "Fahrenheit":
            temp = (value - 32) * 5/9
        elif unit_from == "Kelvin":
            temp = value - 273.15
        
        if unit_to == "Celsius":
            return temp
        elif unit_to == "Fahrenheit":
            return (temp * 9/5) + 32
        elif unit_to == "Kelvin":
            return temp + 273.15
    else:
        return value * (conversions[category][unit_to] / conversions[category][unit_from])


st.markdown(
    "<h1 style='text-align: center;'>Unit Converter</h1>", 
    unsafe_allow_html=True
)

category = st.selectbox("📌 Select Measurement Category:", conversions.keys())
unit_from = st.selectbox("📏 Convert From: ", list(conversions[category].keys()),key="unit_from")
unit_to = st.selectbox("📏 Convert To: ", list(conversions[category].keys()),key="unit_to")
value = st.number_input("✏️ Enter Value:", value=1.0,step=1.0)

if st.button("🚀 Convert Now"):
    result = convert_units(value, unit_from,unit_to,category)
    st.success(f"✅ **{value} {unit_from} = {result:.3f} {unit_to}**")

st.markdown(
    "<h1 style='text-align:center'>Developed By Ibad Ur Rehman</h1>",
    unsafe_allow_html=True
)