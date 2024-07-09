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

# Depth
min_depth = np.round(df['Depth (km)'].min(), 1)
max_depth = np.round(df['Depth (km)'].max(), 1)
start_depth, end_depth = st.select_slider(
    "Depth (km)",
    options = np.round(np.arange(min_depth, max_depth + 1, 1), 1),
    value=(min_depth,max_depth))

# Date
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
min_date = df['Date'].min()
max_date = df['Date'].max()


st.write(min_date)
st.write(max_date)

st.markdown(pd.date_range(min_date, max_date + pd.Timedelta(days=1), freq='D'))


start_date, end_date = st.select_slider(
    "Date",
    options = pd.date_range(min_date, max_date + pd.Timedelta(days=1), freq='D'),
    value=(min_date,max_date))





df_filter = df[(df['Magnitude'] >= start_magnitude) & (df['Magnitude'] <= end_magnitude) & (df['Depth (km)'] >= start_depth) & (df['Depth (km)'] <= end_depth)]



st.markdown(f' Table count {len(df_filter)} / {len(df)} ')
st.write(df_filter)
#st.dataframe(df_filter)






