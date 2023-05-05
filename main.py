import streamlit as st

st.title("Weather Forecast for the Next Days")
place = st.text_input('Place: ')
days = st.slider("Forecast days: ", min_value=1, max_value=5,
                 help="Select the number of forecast days")
option = st.selectbox("Selece data to view",
                      ("Temperatures", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")








