import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox, subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider(
    "Forecast Days:", min_value=1, max_value=5, help="Select number of Forecasted days"
)
option = st.selectbox("Select Data to View", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place} ")

if place:
    try:
        # Get the temperature/Sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            # Create the temperature plot
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(
                x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"}
            )
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "iamges/snow.png",
            }
            image_path = [images[condition] for condition in sky_conditions]
            st.image(image_path, width=115)
    except KeyError:
        st.info("This place data is not available. Please enter the different name.")
