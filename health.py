import pandas as pd
import streamlit as st
import matplotlib.pyplot as pt
import numpy as np
import seaborn as sns 


#import my csv file
df = pd.read_csv("diabetes.csv")
st.markdown ("# first five items")
st.write(df.head())

st.markdown("# Last Ten Items")
st.write(df.tail (10))


st.title("General information About Diabetes Analysis")
 hall = df.describe
 st.write (hall)


 st. title("Blood pressure chart")
 counted = df("Blood pressure Chart")

 st.markdown ("##  overview")
 st.markdown ("first 5 observations")
 st.write(df.head())

 st.markdown ("## Univariate Analysis")

 st.markdown ()