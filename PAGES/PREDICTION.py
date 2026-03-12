import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("Loan Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income")
coapplicant_income = st.number_input("Coapplicant Income")
loan_amount = st.number_input("Loan Amount")
loan_term = st.number_input("Loan Amount Term (in months)")
credit_history = st.selectbox("Credit History", [1, 0])

if st.button("Predict"):
    # Map categorical inputs to numbers as done in training
    gender_val = 1 if gender == "Male" else 0
    married_val = 1 if married == "Yes" else 0
    credit_val = int(credit_history)

    # Create input array
    input_data = np.array([[gender_val, married_val, applicant_income, coapplicant_income, loan_amount, loan_term, credit_val]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Denied")
