import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("linear_regression_model.pkl")

# Streamlit UI
st.set_page_config(page_title="House Price Prediction", layout="centered")
st.title("🏠 House Price Prediction")

st.write("Enter the details below to predict the house price:")

# Input fields matching model training
square_feet = st.number_input("Total Area in Square Feet", min_value=100, step=50)
num_bedrooms = st.slider("Number of Bedrooms", 1, 10)
num_bathrooms = st.slider("Number of Bathrooms", 1, 5)
has_garage = st.selectbox("Has Garage", [0, 1])  # 0 = No, 1 = Yes
year_built = st.number_input("Year Built", min_value=1900, max_value=2025, value=2010)

# Predict button
if st.button("Predict"):
    input_data = np.array([[square_feet, num_bedrooms, num_bathrooms, has_garage, year_built]])
    prediction = model.predict(input_data)
    st.success(f"💰 Predicted House Price: ₹ {prediction[0]:,.2f}")
