# -*- coding: utf-8 -*-
#######################
# Import libraries
import streamlit as st
import pandas as pd
import json
#import altair as alt
import plotly.express as px

#######################
# Page configuration
st.set_page_config(
    page_title="Poland data",
    page_icon=":seedling:",
    layout="wide",
    initial_sidebar_state="expanded")

#alt.themes.enable("dark")


#Data
with open('../data/woj_medium.geojson') as f:
    poland_geojson = json.load(f)

dfd = pd.read_csv('../data/test_data.csv', sep=';', encoding='utf-8', quotechar='"')

kody = dfd['Kod']
print(dfd)


# Sidebar
with st.sidebar:
    st.title(':seedling: Poland data')
    #selected_column_id = st.selectbox('Select a column id', list(dfd.columns))
    selected_column_value = st.selectbox('Select a column value', list(dfd.columns), index=2)
    


    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)



#Map

df = pd.DataFrame(dfd)



def make_choropleth(input_df,input_color_theme, selected_column_id, selected_column_value):
    fig = px.choropleth(
        df,
        geojson=poland_geojson,
        locations='Kod',
        featureidkey='properties.kod',
        color=selected_column_value,
        color_continuous_scale=input_color_theme,
        range_color=(0, max(dfd[selected_column_value])),
        labels={selected_column_value: selected_column_value},
        projection="mercator"
    )

    fig.update_geos(fitbounds="locations", visible=True)
    fig.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=350,
        geo=dict(
            projection_scale=2,
            center={"lat": 52, "lon": 19},
            visible=True
        )

    )

    return fig



#col = st.columns((1.5, 5, 2), gap='medium')


#with col[1]:
st.markdown('#### Data')
    
choropleth = make_choropleth('df_selected_year', selected_color_theme,'selected_column_id', selected_column_value)
st.plotly_chart(choropleth, use_container_width=True)
    


