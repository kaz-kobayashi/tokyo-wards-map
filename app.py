import streamlit as st
import pandas as pd
import pydeck as pdk

# Load wards data
wards = pd.read_csv('wards.csv')

# Calculate average latitude and longitude for initial view
avg_lat = wards['緯度'].mean()
avg_lon = wards['経度'].mean()

# Define the ScatterplotLayer
layer = pdk.Layer(
    "ScatterplotLayer",
    data=wards,
    get_position="[経度, 緯度]",
    get_radius=200,
    get_fill_color=[255, 0, 0],
    pickable=True,
)

# Set the viewport location
view_state = pdk.ViewState(latitude=avg_lat, longitude=avg_lon, zoom=10)

# Render the deck.gl map in Streamlit
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
