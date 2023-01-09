import streamlit as st

st.write("Dataset Overview For Good/Bad Loan")
st.write("'term' : The number of payments on the loan, where values are in months and can be either 36 or 60.")
st.write("'int_rate :  The interest rate on the loan")
st.write("'sub_grade  : Assigned loan subgrade score based on borrower's credit history")
st.write("'emp_length': Borrow's employment length in years.")
st.write("'dti' : A ratio calculated using the borrower's total monthly debt payments on the total debt obligations, excluding mortgage, divided by the borrower's monthly income")
st.write("'mths_since_recent_inq': Months since most recent inquiry")
st.write("'revol_util' : Revolving line utilization rate, or the amount of credit the borrower uses relative to all available revolving credit")
st.write("'bc_util': Ratio of total current balance to high credit/credit limit for all bankcard accounts")
st.write("'num_op_rev_tl' : Number of open revolving accounts")

st.write("We have a lot of features but we got this top 9 features using Logistic Regression with SequentialFeatureSelector")



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/home/gaurav/Documents/BOB/static/accepted_2007_to_2018Q4.csv")

st.write(df)

df['loan_status'].value_counts()

df = df[(df['loan_status'] == 'Fully Paid') | (df['loan_status'] == 'Charged Off')]


final_features = ['term','int_rate','sub_grade','emp_length','dti','mths_since_recent_inq','revol_util','bc_util','num_op_rev_tl','loan_status']

df = df[final_features]

df_temp = df.copy()
st.write(df_temp)
df_temp['loan_status'] = pd.get_dummies(df_temp['loan_status'], drop_first=True)
df_temp['dummies_sub_grade'] = pd.get_dummies(df['sub_grade'], drop_first=True)
df['term'] = df['term'].apply(lambda x: int(x[0:3]))
df_temp['dummies_term'] = pd.get_dummies(df['term'], drop_first=True)
df['loan_status'] = df['loan_status'].map({'Fully Paid':1,'Charged Off':0})

 
