# streamlit_app.py
import streamlit as st
import requests

st.title("Diabetes Prediction App")

inputs = []
features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
for feature in features:
    inputs.append(st.number_input(f"{feature}", step=1.0 if feature != 'Pregnancies' else 1))

if st.button("Predict"):
    response = requests.post("http://127.0.0.1:8000/predict", json={"features": inputs})
    st.write("Prediction:", "Diabetic" if response.json()['prediction'] else "Non-Diabetic")
