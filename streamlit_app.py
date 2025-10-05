import numpy as np
import pandas as pd
import streamlit as st

st.title("Machine Learning App")
st.info("This app is to build Machine learning Module")
df = pd.read_csv("Raw_data.csv")
df.head
