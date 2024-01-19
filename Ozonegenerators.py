import streamlit as st
import pandas as pd
import numpy as np
import math
from PIL import Image

#@st.cache

def round_half_up(n, decimals=0):
    multiplier = 5 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

#im = chart_with_upwards_trend
st.set_page_config(
    page_title="Calculadora VES",
    #page_icon=im,
)

st.image("https://i.imgur.com/y6j7fR4.jpg")
st.image("https://i.imgur.com/1FOeg53.png")



st.write("----------------------------------------------------------------------------------------------------")

st.markdown("<p style='text-align: center; color:gray; font-size: 14px;'> © 2022 Reserve <br> Rev. 1.03 </p>", unsafe_allow_html=True)
