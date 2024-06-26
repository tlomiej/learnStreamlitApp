import streamlit as st
import pandas as pd
import json
import plotly.express as px

dev = False
path = './../' if dev else ''


if 'sample_data' not in st.session_state:
    st.session_state.sample_data = False


st.set_page_config(
    page_title="Poland GUS data",
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

#Map

def make_choropleth(input_df,input_color_theme, selected_column_id, selected_column_value):
    fig = px.choropleth(
        df,
        geojson=poland_geojson,
        locations='Kod',
        featureidkey='properties.kod',
        color=selected_column_value,
        color_continuous_scale=input_color_theme,
        range_color=(min(dfd[selected_column_value]), max(dfd[selected_column_value])),
        labels={selected_column_value: 'Value'},
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
            projection_scale=6,
            center={"lat": 52, "lon": 19},
            visible=True
        )

    )

    return fig

if df is not None:
    dfd = pd.DataFrame(df, columns=['Kod', "Nazwa", selected_column_value ])
    selected_columns = df[['Kod', "Nazwa", selected_column_value ]]


if uploaded_file is not None and st.session_state.sample_data == False:
    tab1, tab2 = st.tabs(["Map", "Table"])

    with tab1:
        st.markdown(f'#### {selected_column_value}')
        choropleth = make_choropleth('df_selected_year', selected_color_theme,'selected_column_id', selected_column_value)
        st.plotly_chart(choropleth, use_container_width=True)
        col1, col2 = st.columns(2, gap='small')
        col1.metric(label="Min", value=min(dfd[selected_column_value]))
        col2.metric(label="Max", value=max(dfd[selected_column_value]))
    with tab2:
        st.dataframe(selected_columns) 

elif uploaded_file is None and st.session_state.sample_data == True:
    tab1, tab2 = st.tabs(["Map", "Table"])

    with tab1:
        st.markdown(f'''#### Sample Data ''')
        st.markdown(f'#### {selected_column_value}')
        choropleth = make_choropleth('df_selected_year', selected_color_theme,'selected_column_id', selected_column_value)
        st.plotly_chart(choropleth, use_container_width=True)
        col1, col2 = st.columns(2, gap='small')
        col1.metric(label="Min", value=min(dfd[selected_column_value]))
        col2.metric(label="Max", value=max(dfd[selected_column_value]))

    with tab2:
        st.dataframe(selected_columns) 
else:
    
    st.markdown(f'''#### Download data from    {st.session_state.sample_data}''')
    st.markdown(f"[Here](https://bdl.stat.gov.pl/bdl/dane/podgrup/temat)")
    st.markdown("and load.")

    st.button("Show sample data", on_click=show_sample_data)
        


