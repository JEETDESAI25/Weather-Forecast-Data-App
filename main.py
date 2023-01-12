import streamlit as st
import plotly.express as px 
from backend import get_data

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place:")
days = st.slider("Forecast Days:", min_value=1, max_value=5, help="Select number of Forecasted days")
option = st.selectbox("Select Data to View", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place} ")



# data = get_data(place, days, option):



# figure = px.line(x=, y=, labels={})
# st.plotly_chart(figure)