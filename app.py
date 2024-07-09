import streamlit as st
from streamlit_folium import st_folium
from main import display_map

st.set_page_config(page_title="Testing Folium")

st.title("Map")

st_folium(display_map())