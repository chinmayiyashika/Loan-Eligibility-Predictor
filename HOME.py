import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# TITLE AND DESCRIPTION
# -------------------------
st.title("Loan Approval Prediction System")

st.image("https://cdn-icons-png.flaticon.com/512/3135/3135706.png", width=150)

st.write("""
This web application predicts whether a loan application will be approved 
or rejected based on applicant details such as income, loan amount, 
and credit history.
""")

st.info("Use the sidebar to navigate to the Prediction and Dataset pages.")

# -------------------------
# LOAD DATA
# -------------------------
df = pd.read_csv("train.csv")

# -------------------------
# METRICS
# -------------------------
st.subheader("Loan Application Overview")

total_apps = len(df)
approved = (df["Loan_Status"] == "Y").sum()
rejected = (df["Loan_Status"] == "N").sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Applications", total_apps)
col2.metric("Approved Loans", approved)
col3.metric("Rejected Loans", rejected)

# -------------------------
# VISUALIZATIONS
# -------------------------
st.subheader("Loan Data Insights")

# Pie Chart
fig1, ax1 = plt.subplots()
loan_counts = df["Loan_Status"].value_counts()

ax1.pie(
    loan_counts,
    labels=["Approved", "Rejected"],
    autopct='%1.1f%%'
)

ax1.set_title("Loan Approval Distribution")

# Box Plot
fig2, ax2 = plt.subplots()
df.boxplot(column="ApplicantIncome", by="Loan_Status", ax=ax2)
ax2.set_title("Income vs Loan Approval")
ax2.set_ylabel("Applicant Income")
plt.suptitle("")

# Credit History vs Loan Approval
fig3, ax3 = plt.subplots()
credit_data = pd.crosstab(df["Credit_History"], df["Loan_Status"])
credit_data.plot(kind="bar", ax=ax3)
ax3.set_title("Credit History vs Loan Approval")
ax3.set_xlabel("Credit History")
ax3.set_ylabel("Count")

# Loan Amount Distribution
fig4, ax4 = plt.subplots()
ax4.hist(df["LoanAmount"].dropna(), bins=30)
ax4.set_title("Loan Amount Distribution")
ax4.set_xlabel("Loan Amount")

# Scatter Plot
fig5, ax5 = plt.subplots()
ax5.scatter(df["ApplicantIncome"], df["LoanAmount"])
ax5.set_title("Income vs Loan Amount")
ax5.set_xlabel("Applicant Income")
ax5.set_ylabel("Loan Amount")

# -------------------------
# DASHBOARD LAYOUT
# -------------------------
col1, col2 = st.columns(2)

with col1:
    st.pyplot(fig1)

with col2:
    st.pyplot(fig2)

col3, col4 = st.columns(2)

with col3:
    st.pyplot(fig3)

with col4:
    st.pyplot(fig4)

st.pyplot(fig5)