import streamlit as st
import pandas as pd
import numpy as np



st.markdown("Earthquakes!")

st.markdown("Source data : https://www.kaggle.com/datasets/stealthtechnologies/earthquakes-dataset")


df = pd.read_csv('data/data.csv')


# Magnitude
min_magnitude = np.round(df['Magnitude'].min(), 1)
max_magnitude = np.round(df['Magnitude'].max(), 1)
start_magnitude, end_magnitude = st.select_slider(
    "Magnitude",
    options = np.round(np.arange(min_magnitude, max_magnitude + 0.1, 0.1), 1),
    value=(min_magnitude,max_magnitude))


st.write(start_magnitude)
st.write(end_magnitude)


st.dataframe(df)






