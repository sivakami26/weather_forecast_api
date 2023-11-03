import streamlit as st
import plotly.express as px
import backend



st.title("Weather forecast for the Next Days")

place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
if place:
    try:
        data = backend.get_data(place, days)
        date = [item["dt_txt"] for item in data]
        if option == "Temperature":
            temp = [item["main"]["temp"] /10 for item in data]
            figure = px.line(x=date, y=temp, labels={"x":"Date", "y":"Temperature (C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            filtered_data = [item["weather"][0]["main"] for item in data]
            for item, date_info in zip(filtered_data, date):
                st.subheader(date_info)
                st.image(f"images/{item.lower()}.png", width=200)
    except KeyError:
        st.text("Entered city is invalid")



