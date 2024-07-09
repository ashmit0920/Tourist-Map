import folium

def display_map():
    # Create a map centered at a specific latitude and longitude
    mymap = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

    # Add a marker
    folium.Marker([45.5236, -122.6750], popup='Portland, OR').add_to(mymap)

    # Display the map
    return mymap