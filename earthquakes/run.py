import streamlit as st
import pandas as pd



st.markdown("Earthquakes!")

st.markdown("Source data : https://www.kaggle.com/datasets/stealthtechnologies/earthquakes-dataset")


df = pd.read_csv('data/data.csv')

st.dataframe(df)






