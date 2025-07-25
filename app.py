import streamlit as st
import joblib

# Load the trained model
model = joblib.load("linear_regression_model.pkl")

st.title("House Price Prediction")

# Input fields
bhk = st.number_input("Number of BHK", min_value=1, max_value=10)
balcony = st.number_input("Number of Balconies", min_value=0, max_value=5)
area = st.number_input("Area (sqft)", min_value=100)

# Predict button
if st.button("Predict Price"):
    features = [[bhk, balcony, area]]
    prediction = model.predict(features)
    st.success(f"Predicted Price: ₹ {prediction[0]:,.2f}")
