import pandas as pd
import streamlit as st
import matplotlib.pyplot as pt
import numpy as np
import seaborn as sns 


#import my csv file
df = pd.read_csv("diabetes.csv")


st.markdown ("## overview")


st.write(df.head())

st.markdown("### first 5 observations")
st.write(df.head ())


st.markdown("### Last observation 5 observations")
st.markdown(df.tail())

st.markdown("### Description  of Numeric data types")
st.write(df.describe())

st.markdown("## Data shape")
st.write(df.shape)


st.markdown ("## univariate Analysis")

st.markdown ("### Blood Pressure")

st.write (df["BloodPressure"].describe())
          

           
bp= px.bar(df['BloodPressure'], y = 'BloodPressure',title="Distribution of Blood Pressure")

st.plotly_chart(bp, use_container_width=True)





st.markdown ("## Bivarate Analysis")

st.markdown("Blood Pressure vs pregnancies")

df2 = pd.Dataframe(df["BloodPressure"], df['pregnanacies'])
st.write(df2)




bp2 = px.histogram(df2, x= "pregenancies", y='Bloodpressure',
title="Distribution of pregenancies vs Bloood pressure")

st.plotly_chart(bp2, use_conatiner_width=True)