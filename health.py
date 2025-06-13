import pandas as pd
import streamlit as st
import matplotlib.pyplot as pt
import numpy as np
import seaborn as sns 


#import my csv file
df = pd.read_csv("diaabetes.csv")
st.write(df.head)