import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("model.pkl")

# App title
st.title("🩺 Diabetes Risk Prediction App")
st.write("Enter the details below to predict the risk of diabetes.")

# Input form
pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose Level", min_value=0)
blood_pressure = st.number_input("Blood Pressure", min_value=0)
skin_thickness = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0, format="%.1f")
diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
age = st.number_input("Age", min_value=1)

# Predict button
if st.button("Predict"):
    # Create a DataFrame with input values
    input_data = pd.DataFrame(
        [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]],
        columns=["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", 
                 "DiabetesPedigreeFunction", "Age"]
    )
    
    # Make prediction
    prediction = model.predict(input_data)

    # Output result
    if prediction[0] == 1:
        st.error("⚠️ High Risk of Diabetes!")
    else:
        st.success("✅ Low Risk of Diabetes.")

