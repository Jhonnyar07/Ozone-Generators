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
    page_title="Calculo de Generadores de Ozono",
    #page_icon=im,
)

st.image("https://i.imgur.com/fhOBqO5.jpg")

#Selecting the calcule for Ozone gas or water
option=st.selectbox('Tipo de instalación:', ('Ozono Ambiente', 'Ozono Agua'), index=None)

if option == "Ozono Agua":
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        Vr = st.number_input("Volumen del recipiente (Litros)")
    with col2:
        Qc = st.number_input("Caudal de consumo en producción (m3/h)")
    with col3:
        Qr = st.number_input("Caudal de recirculación (m3/h)")
    with col4:
        C = st.text_input("Concentración objetivo de Ozono Disuelto")







st.write("----------------------------------------------------------------------------------------------------")

st.markdown("<p style='text-align: center; color:gray; font-size: 14px;'> © 2024 PID Medioambiental, S.L. <br> Rev. 1.03 </p>", unsafe_allow_html=True)
