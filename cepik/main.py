import streamlit as st
import time
import requests

searchText = st.text_input('Search')
searchData = []

def getData(text):
    time.sleep(4)
    url = 'https://api.github.com/users/mralexgray/repos'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
        
    else:
        print(f"Failed to retrieve data: {response.status_code}")
    return [1,2,3,4,5,text]

def clear_search_fields():
    searchText = ''



placeholder = st.empty()
btn = placeholder.button('Find', disabled=False, key='search1')
if btn:
    placeholder.button('Find...', disabled=True, key='search2')
    searchData.append(getData(searchText))
    
    

    #placeholder.button('Clear', disabled=False, key='search3', on_click=clear_search_fields)



st.write(searchData)










# - search object 
# wojewodztwo - multiselect
# data_od - data-do


#https://api.cepik.gov.pl/pojazdy?wojewodztwo=06&data-od=20180101&data-do=20191231
# insert tu numpy dataset
# display table





