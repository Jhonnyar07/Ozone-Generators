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
    col1,col2,col3 = st.columns(3)
    with col1:
        st.write("Factor de seguridad por transferencia de masa")
        st.write("0.9")
    with col2:
        st.write("Factor de seguridad por rendimiento de generación")
        st.write("0.8")
    with col3:
        st.write("Factor de seguridad general de diseño")
        st.write("1.5")
        
    
    col4,col5,col6,col7 = st.columns(4)
    with col4:
        Vr = st.number_input("Volumen del recipiente (Litros)", value=None)
    with col5:
        Qc = st.number_input("Caudal de consumo en producción (m3/h)", value=None)
    with col6:
        Qr = st.number_input("Caudal de recirculación (m3/h)", value=None)
    with col7:
        C = st.number_input("Concentración objetivo de Ozono Disuelto (PPM)", value=None)
    calcule = st.button("Calcular",use_container_width=True)
    if calcule == True:
        col8,col9,col10= st.columns(3)
        with col8:
            







st.write("----------------------------------------------------------------------------------------------------")

st.markdown("<p style='text-align: center; color:gray; font-size: 14px;'> © 2024 PID Medioambiental, S.L. <br> Rev. 1.03 </p>", unsafe_allow_html=True)
