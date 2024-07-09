import streamlit as st
import folium
from streamlit_folium import st_folium

mymap = folium.Map(location=[48.8566, 2.3522], zoom_start=13)  # Centered on Paris, France

tourist_spots = {
    "Eiffel Tower": [48.8584, 2.2945],
    "Louvre Museum": [48.8606, 2.3376],
    "Notre-Dame Cathedral": [48.8529, 2.3500],
}

for spot, coords in tourist_spots.items():
    folium.Marker(coords, popup=spot).add_to(mymap)

st.title("Tourist Map of Paris")
st_folium(mymap, width=700, height=500)