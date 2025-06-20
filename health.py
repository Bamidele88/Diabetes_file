import pandas as pd
import streamlit as st
import matplotlib.pyplot as pt
import numpy as np
import seaborn as sns 
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


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
          

           
bp = px.bar(df['BloodPressure'], y ='BloodPressure', title="Distribution of Blood Pressure")

st.plotly_chart(bp, use_container_width =True)





st.markdown (" BIVARIATE ANALYSIS")
st.markdown("##Blood Pressure vs Age Description")
df2 = pd.Dataframe(df["BloodPressure"], df["Age"])
st.write(df2)

st.markdown("## BloodPressure vs Insulin")
df3 = pd.DataFrame(df["BloodPressure"], df["Insulin"])
st.write(df3)




bp2 = px.histogram(df2, x= "Age", y='Bloodpressure',
title="Distribution of Age vs Bloood pressure")

st.plotly_chart(bp2, use_conatiner_width=True)



#PREDICTIVE DATA ANALYSIS(PREDICTION)
st.markdown("##PREDICTICE ANALYSIS")
#use drop function to select the column to predict
x = df.drop("Outcome", axis=1)
Y= df["Outcome"]

x_train,x_test,Y_train,Y_test = train_test_split(x,Y,test_size=0.2)

model = LogisticRegression()
model.fit(x_train,Y_train)

prediction = model.predict(x_test)


st.write(prediction)


st.markdown("## Model Evaluation")
accuracy = accuracy_score(prediction, Y_test)
st.write(accuracy)