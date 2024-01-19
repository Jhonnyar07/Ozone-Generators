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
    st.divider()
    st.markdown("<h3 style='text-align: center;'>Factores de seguridad de diseño</h3>", unsafe_allow_html=True)
    col1,col2,col3 = st.columns(3)
    with col1:
        st.markdown("<p style='text-align: center;'>Factor de seguridad por transferencia de masa</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>0.9</p>", unsafe_allow_html=True)
    with col2:
        st.markdown("<p style='text-align: center;'>Factor de seguridad por rendimiento de generación</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>0.8</p>", unsafe_allow_html=True)
    with col3:
        st.markdown("<p style='text-align: center;'>Factor de seguridad general de diseño</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>1.5</p>", unsafe_allow_html=True)

    st.divider()

    st.markdown("<h3 style='text-align: center;'>Parámetros de diseño</h3>", unsafe_allow_html=True)
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

#Parameters Calcule
    
    if calcule == True:
        st.divider()
        st.markdown("<h3 style='text-align: center;'>Resultados</h3>", unsafe_allow_html=True)
        col8,col9,col10 = st.columns(3)
        with col8:
            st.markdown("<p style='text-align: center;'>Tiempo de tratamiento completo vaso principal (min)</p>", unsafe_allow_html=True)
            Tt = float("{:.2f}".format(Qc/(Vr/1000))
            st.button(Tt,use_container_width=True)
        with col9:
            st.markdown("<p style='text-align: center;'>Tiempo de recirculacion en tanque (h)</p>", unsafe_allow_html=True)
            Tr = float("{:.2f}".format((Vr/1000)/Qr)
            st.button(Tr,use_container_width=True)      
        with col10:
            st.markdown("<p style='text-align: center;'>Producción mínima esperada (g/h)</p>", unsafe_allow_html=True)
            Pe = float("{:.2f}".format((C*Qc))
            st.button(Pe,use_container_width=True)
        st.markdown("<h3 style='text-align: center;'>Producción requerida (g/h)</3>", unsafe_allow_html=True)
        Pr = float("{:.2f}".format((1.5*Pe)/(0.8*0.9)))
        st.button(Pr,use_container_width=True)
        



st.write("----------------------------------------------------------------------------------------------------")

st.markdown("<p style='text-align: center; color:gray; font-size: 14px;'> © 2024 PID Medioambiental, S.L. <br> Rev. 1.01 </p>", unsafe_allow_html=True)
