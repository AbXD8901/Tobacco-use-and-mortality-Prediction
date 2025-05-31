import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load('xgb_model.pkl')

st.title("Tobacco Mortality Prediction App")

st.markdown("""
Enter the following information to predict whether a disease case will result in **Mortality** or not.
""")

# Input fields
year = st.number_input("Year", min_value=2004, max_value=2020, step=1)
tobacco_price = st.number_input("Tobacco Price Index")
affordability = st.number_input("Affordability of Tobacco Index")
income = st.number_input("Real Household Disposable Income")
all_prescriptions = st.number_input("All Pharmacotherapy Prescriptions", step=1)
nrt_prescriptions = st.number_input("Nicotine Replacement Therapy Prescriptions", step=1)

# Disease Category Dropdown (Label Encoded: 6-Cancer, ..., 0-Injury)
disease_map = {
    'Cancer': 6,
    'Respiratory': 5,
    'Circulatory': 4,
    'Digestive': 3,
    'Eye/Ear': 2,
    'Reproductive': 1,
    'Injury': 0
}
disease_input = st.selectbox("Disease Category", options=list(disease_map.keys()))
disease_encoded = disease_map[disease_input]

# Make prediction
if st.button("Predict Mortality"):
    input_data = pd.DataFrame([[
        year, tobacco_price, affordability, income,
        all_prescriptions, nrt_prescriptions, disease_encoded
    ]], columns=[
        'Year', 'Tobacco Price Index', 'Affordability of Tobacco Index',
        'Real Households\' Disposable Income',
        'All Pharmacotherapy Prescriptions',
        'Nicotine Replacement Therapy (NRT) Prescriptions',
        'Disease Category'
    ])

    prediction = model.predict(input_data)[0]
    result = "Mortality (Yes)" if prediction == 1 else "No Mortality"
    st.success(f"Prediction: **{result}**")
