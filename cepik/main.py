import streamlit as st
import requests
import time



def get_data():
    try:
        url = 'https://api.cepik.gov.pl/pojazdy?wojewodztwo=14&data-od=20180101'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            st.session_state.displayResult = True
            st.session_state.searchData = data  
        else:
            st.session_state.searchData = response.status_code
    except Exception as e:
        st.session_state.searchData = e


if 'searchData' not in st.session_state:
    st.session_state.searchData = []
if 'displayResult' not in st.session_state:
    st.session_state.displayResult = False

if 'text_input' not in st.session_state:
    st.session_state.text_input = ''

if 'search_in_progress' not in st.session_state:
    st.session_state.search_in_progress = False


def clear_search_fields():
    st.session_state.searchData = []
    st.session_state.displayResult = False
    st.session_state.text_input = ''
    st.session_state.search_in_progress = False


def clear_text():
    st.session_state.text_input = ''


#st.text_input("Enter some text:", key='text_input')
st.text_input('Search', key='text_input')

col1, col2 = st.columns(2)

col1.button('Search', disabled=False, key='search', on_click=get_data)
col2.button('Clear', disabled=False, key='clear', on_click=clear_search_fields)


#if st.session_state.displayResult:
st.write(st.session_state.searchData)
#else:
#    st.write('fff')











# - search object 
# wojewodztwo - multiselect
# data_od - data-do


#https://api.cepik.gov.pl/pojazdy?wojewodztwo=06&data-od=20180101&data-do=20191231
# insert tu numpy dataset
# display table





