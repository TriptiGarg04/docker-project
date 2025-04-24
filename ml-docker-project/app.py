import streamlit as st
import pandas as pd
import pickle

# Load the trained ML model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.title("🍄 Mushroom Classification App")
st.write("Enter mushroom characteristics to predict if it's edible or poisonous!")

# User input features
cap_shape = st.selectbox("Cap Shape", ["bell", "conical", "flat", "knobbed", "sunken"])
cap_color = st.selectbox("Cap Color", ["brown", "yellow", "white", "gray", "red"])

# Make a prediction
if st.button("Predict"):
    # Convert input to model format
    input_data = [[cap_shape, cap_color]]
    prediction = model.predict(input_data)
    result = "Edible 🍽️" if prediction[0] == 0 else "Poisonous ☠️"
    
    st.subheader(f"Prediction: {result}")
