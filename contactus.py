import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data=pd.read_csv("tips.csv")
st.write("Sales Daily Chart")
st.line_chart(data,x="billdate",y="total_bill")

st.divider()
st.scatter_chart(data,x="tip",y="total_bill")
st.divider()

fig, ax = plt.subplots()
ax.hist(data["tip"])

st.pyplot(fig)

st.divider()

a=st.number_input("What is your salary? ")
b=st.number_input("How much is your monthly tax? ")
if st.button("CALCULATE"):
    c=a-b
else:
    c=0.00
st.write("My net salary is ", c)



