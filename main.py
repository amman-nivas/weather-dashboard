import streamlit as st
import pandas as pd
import numpy as np
import requests
import time

st.snow()
# st.write ('Loheith')
st.title ('My Weather Dashboard')

resp = requests.get('https://api.open-meteo.com/v1/forecast?latitude=6.9355&longitude=79.8487&current=temperature_2m,relative_humidity_2m,is_day,precipitation,wind_speed_10m,wind_direction_10m,wind_gusts_10m&hourly=temperature_2m,rain,wind_direction_120m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,wind_direction_10m_dominant')
value =resp.json()

col1, col2, col3= st.columns(3)
col1.metric ( "Tempeature",value['current']['temperature_2m'])
col2.metric ('Precipitation',value['current']['precipitation']) 
col3.metric ('Wind Speed',value['current']['wind_speed_10m'])
weather= pd.DataFrame(value['daily']['precipitation_sum'], value['daily']['time'])

st.subheader('_RAINFALL DATA_:sunglasses:')

st.bar_chart(weather)


st.sidebar.image('flag.jpg')


st.sidebar.write('Latitude',value['latitude'])
st.sidebar.write('Longitude',value['longitude'])

st.video('https://www.youtube.com/watch?v=-nc146I26SU')

col4, col5= st.sidebar.columns(2)
col4.metric ('WIND GUSTS',value['current']['wind_gusts_10m'])
col5.metric('WIND DIRECTION',value['current']['wind_direction_10m'])
st.sidebar.metric('HUMIDITY',value['current']['relative_humidity_2m'])