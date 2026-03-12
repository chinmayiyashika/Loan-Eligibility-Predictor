import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# load dataset
df = pd.read_csv("train.csv")

# convert text values to numbers
df["Gender"] = df["Gender"].map({"Male":1, "Female":0})
df["Married"] = df["Married"].map({"Yes":1, "No":0})
df["Education"] = df["Education"].map({"Graduate":1, "Not Graduate":0})
df["Self_Employed"] = df["Self_Employed"].map({"Yes":1, "No":0})
df["Property_Area"] = df["Property_Area"].map({"Urban":2, "Semiurban":1, "Rural":0})
df["Loan_Status"] = df["Loan_Status"].map({"Y":1, "N":0})

# select features
X = df[[
"Gender",
"Married",
"ApplicantIncome",
"CoapplicantIncome",
"LoanAmount",
"Loan_Amount_Term",
"Credit_History"
]]

# target
y = df["Loan_Status"]

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# save model
pickle.dump(model, open("model.pkl","wb"))

print("Model trained successfully!")