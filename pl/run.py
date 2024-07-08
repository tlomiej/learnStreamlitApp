from utiles import make_choropleth
import streamlit as st
import pandas as pd
import json
import plotly.express as px

from components.sample_component.my_component import my_component
from components.discreat_slider import discreat_slider

dev = True
path = './../' if dev else ''


if 'sample_data' not in st.session_state:
    st.session_state.sample_data = False


st.set_page_config(
    page_title="GUS data",
    page_icon=":seedling:",
    layout="wide",
    initial_sidebar_state="expanded")


#Data
with open(f'{path}data/woj_medium.geojson') as f:
    poland_geojson = json.load(f)


def show_sample_data():
    st.session_state.sample_data = True

def on_change_file():
    st.session_state.sample_data = False

df = None
# Sidebar
with st.sidebar:
    st.title(':seedling: Poland GUS data')

    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv", on_change=on_change_file)

    # Wczytanie danych z pliku
    if uploaded_file is not None or st.session_state.sample_data:

        df = pd.read_csv(f'{path}data/test_data.csv' if st.session_state.sample_data else uploaded_file, sep=';', encoding='utf-8', quotechar='"')

        selected_column_value = st.selectbox('Select a column value', list(df.columns), index=2)
        if df[selected_column_value].isnull().any():
            st.warning(f"There is no data. Select another column")

        color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
        selected_color_theme = st.selectbox('Select a color theme', color_theme_list)
    else:
        st.session_state.sample_data = False


discreat_slider('test', 'aaa')

if df is not None:
    dfd = pd.DataFrame(df, columns=['Kod', "Nazwa", selected_column_value ])
    selected_columns = df[['Kod', "Nazwa", selected_column_value ]]


if uploaded_file is not None and st.session_state.sample_data == False:
    tab1, tab2 = st.tabs(["Map", "Table"])

    with tab1:
        st.markdown(f'#### {selected_column_value}')
        choropleth = make_choropleth(dfd, selected_color_theme,'selected_column_id', selected_column_value, poland_geojson)
        st.plotly_chart(choropleth, use_container_width=True)
        col1, col2 = st.columns(2, gap='small')
        col1.metric(label="Min", value=min(dfd[selected_column_value]))
        col2.metric(label="Max", value=max(dfd[selected_column_value]))
    with tab2:
        st.dataframe(selected_columns) 

elif uploaded_file is None and st.session_state.sample_data == True:
    tab1, tab2, tab3 = st.tabs(["Map", "Table", "Custom"])

    with tab1:
        st.markdown(f'''#### Sample Data ''')
        st.markdown(f'#### {selected_column_value}')
        choropleth = make_choropleth(df, selected_color_theme,'selected_column_id', selected_column_value, poland_geojson)
        st.plotly_chart(choropleth, use_container_width=True)
        col1, col2 = st.columns(2, gap='small')
        col1.metric(label="Min", value=min(dfd[selected_column_value]))
        col2.metric(label="Max", value=max(dfd[selected_column_value]))

    with tab2:
        st.dataframe(selected_columns) 
    
    with tab3:
        click_num = my_component('test', key='comp')
        st.markdown(f'{click_num}')

else:
    
    st.markdown(f'''#### Download data from    {st.session_state.sample_data}''')
    st.markdown(f"[Here](https://bdl.stat.gov.pl/bdl/dane/podgrup/temat)")
    st.markdown("and load.")

    st.button("Show sample data", on_click=show_sample_data)
        


