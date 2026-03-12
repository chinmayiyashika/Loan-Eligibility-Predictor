import streamlit as st
import pickle
import numpy as np
import pandas as pd

# -------------------------
# LOAD MODEL
# -------------------------
model = pickle.load(open("model.pkl", "rb"))

st.title("Loan Prediction System")

st.write("Enter applicant details to predict loan eligibility.")

# -------------------------
# INPUT FIELDS (2 COLUMNS)
# -------------------------
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"], index=0)
    married = st.selectbox("Married", ["Yes", "No"], index=0)
    applicant_income = st.number_input("Applicant Income", value=5000)

with col2:
    coapplicant_income = st.number_input("Coapplicant Income", value=2000)
    loan_amount = st.number_input("Loan Amount", value=150)
    loan_term = st.number_input("Loan Amount Term (months)", value=360)

credit_history = st.selectbox("Credit History", [1, 0], index=0)

# -------------------------
# PREDICTION
# -------------------------
if st.button("Predict Loan Eligibility"):

    gender_val = 1 if gender == "Male" else 0
    married_val = 1 if married == "Yes" else 0
    credit_val = int(credit_history)

    input_data = np.array([[
        gender_val,
        married_val,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_val
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Denied")

# -------------------------
# MODEL INFORMATION TABLE
# -------------------------
st.subheader("Model Information")

model_info = {
    "Algorithm": ["Random Forest"],
    "Type of Algorithm": ["Ensemble Learning (Classification)"],
    "Evaluation Metric (F1-Score)": ["0.81"]
}

df = pd.DataFrame(model_info)

st.table(df)