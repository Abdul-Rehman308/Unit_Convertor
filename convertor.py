#Project 01: Unit Convertor
#Build a Google Unit Convertor using Python and Streamlit

import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
    }
    .stButton>button {
        background: linear-gradient(45deg, #0b5394, #351c75);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 225, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg,#92fe9d,#00c9ff);
        colour: black
    }
    .result {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background:rgba(255,255,255,0.1);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0,201,255,0.3);
    }
    footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)
#title and description
st.markdown("<h1>🚀Unit Convertor using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature.")

#sidebar menu
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value",value=0.0,min_value=0.0,step=0.1)
col1,col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From Unit",["Meters","Kilometers","Miles","Feet","Inches","Yards"])
    with col2:
        to_unit = st.selectbox("To Unit",["Meters","Kilometers","Miles","Feet","Inches","Yards"])
    
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From Unit",["Kilograms","Grams","Pounds","Ounces"])
    with col2:
        to_unit = st.selectbox("To Unit",["Kilograms","Grams","Pounds","Ounces"])
        
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From Unit",["Celsius","Fahrenheit","Kelvin"])
    with col2:
        to_unit = st.selectbox("To Unit",["Celsius","Fahrenheit","Kelvin"])

#converted functions

def length_conversion(value,from_unit,to_unit):
    length_units = {
        "Meters":1,
        "Kilometers":0.001,
        "Centimeters":100,
        "Millimeters":1000,
        "Miles":1609.34,
        "Feet":3.28,
        "Inches":39.37,
        "Yards":1.09361,
    }
    return(value / length_units[from_unit]*length_units[to_unit])

def weight_conversion(value,from_unit,to_unit):
    weight_units = {
        "Kilograms":1,
        "Grams":1000,
        "Pounds":2.20462,
        "Ounces":35.274,
    }
    return(value / weight_units[from_unit]*weight_units[to_unit])
def temperature_conversion(value,from_unit,to_unit):
    if from_unit == "Celsius":
        return(value*9/5+32)if to_unit == "Fahrenheit" else value+273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return((value-32)*5/9)if to_unit == "Celsius" else (value-32)*5/9+273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return(value-273.15)if to_unit == "Celsius" else (value-273.15)*9/5+32 if to_unit == "Fahrenheit" else value
    else:
        return value
# Button to perform conversion
if st.button("Convert"):
        if conversion_type == "Length":
            result = length_conversion(value,from_unit,to_unit)
        elif conversion_type == "Weight":
            result = weight_conversion(value,from_unit,to_unit)
        elif conversion_type == "Temperature":
            result = temperature_conversion(value,from_unit,to_unit)
        
        st.markdown(f"<div class='result-box'>{result} {from_unit} = {result:.4f} {to_unit}</div>",unsafe_allow_html=True)
        
        st.markdown("<div class= 'footer'>Created with love by Syed AR /div>",unsafe_allow_html=True )  
    
        

        
