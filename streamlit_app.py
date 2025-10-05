import numpy as np
import pandas as pd
import streamlit as st

st.title("Machine Learning App")
st.info("This app is to build Machine learning Module")

with st.expander("Raw_data"):
  st.write("**DATA**")
  df = pd.read_csv("Raw_data.csv")
  df

  st.write("**X**")
  x = df.drop('species', axis = 1)
  x
  
  st.write("**Y**")
  y = df.species
  y
with st.expander("Data_visulaization"):
  st.scatter_chart(data=df, x= 'bill_length_mm', y= 'body_mass_g', color = 'species' )

# Data Preparations
with st.sidebar:
  st.header("Input Features")
  island = st.selectbox("Island", ('Biscoe', 'Dream', 'Torgersen' ))
  gender = st.selectbox('Gender',('male','female'))
  bill_length_mm = st.slider('Bill Length (mm)', 32.1, 59.6, 43.9)




