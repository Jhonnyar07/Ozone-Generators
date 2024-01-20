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
    page_title="Calculo de Generadores de Ozono"
)

st.image("https://i.imgur.com/fhOBqO5.jpg")

#Selecting the calcule for Ozone gas or water
option=st.selectbox('Tipo de instalación:', ('Ozono Agua','Ozono Ambiente'), index=None)



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
    Pump=st.selectbox('Bomba de recirculación:', ('CM 3-5', 'CM 10-1', 'CM 10-2', 'MATRIX/A 5-6T'), index=None)
    if Pump == 'CM 3-5':
        Co1= 500
        V1= 2740
        Q1= 3.1
        H1 = 34.75
        Pt1= 10
        P1 = float("{:.2f}".format((H1*9.8*1000)/100000))
        D1 = pd.DataFrame({
        'Consumo (Watts)': [Co1],
        'Velocidad (RPM)': [V1],
        'Caudal (m3/h)': [Q1],
        'Altura (m)': [H1],
        'P. trabajo @-22/55 ºC (Bar)': [Pt1],
        'P. Descarga (Bar)': [P1]
        })
        st.dataframe(D1, hide_index=True, use_container_width=True)
        with open("96806804_CM_35_ARAEAVBE_CAAN.pdf", "rb") as file:
            btn = st.download_button(
            label="Ficha Técnica",
            data=file,
            file_name="96806804_CM_35_ARAEAVBE_CAAN.pdf",
            mime="Doc/pdf",
            use_container_width=True
          )
    if Pump == 'CM 10-1':
        Co2= 670
        V2= 2800
        Q2= 10
        H2 = 13.67
        Pt2= 10
        P2 = float("{:.2f}".format((H2*9.8*1000)/100000))
        D2=pd.DataFrame({
        'Consumo (Watts)': [Co2],
        'Velocidad (RPM)': [V2],
        'Caudal (m3/h)': [Q2],
        'Altura (m)': [H2],
        'P. trabajo @-22/55 ºC (Bar)': [Pt2],
        'P. Descarga (Bar)': [P2]
        })
        st.dataframe(D2, hide_index=True, use_container_width=True)
        with open("96806942_CM_101_ARAEAVBE_CAAN.pdf", "rb") as file:
            btn = st.download_button(
            label="Ficha Técnica",
            data=file,
            file_name="96806942_CM_101_ARAEAVBE_CAAN.pdf",
            mime="Doc/pdf",
            use_container_width=True
          )
    if Pump == 'CM 10-2':
        Co3= 1500
        V3= 2910
        Q3= 10
        H3 = 27.09
        Pt3 = 10
        P3 = float("{:.2f}".format((H3*9.8*1000)/100000))
        D3 = pd.DataFrame({
        'Consumo (Watts)': [Co3],
        'Velocidad (RPM)': [V3],
        'Caudal (m3/h)': [Q3],
        'Altura (m)': [H3],
        'P. trabajo @-22/55 ºC (Bar)': [Pt3],
        'P. Descarga (Bar)': [P3]
        })
        st.dataframe(D3, hide_index=True, use_container_width=True)
        with open("98771564_CM_102_ARAEAQQE_FAAN.pdf", "rb") as file:
            btn = st.download_button(
            label="Ficha Técnica",
            data=file,
            file_name="98771564_CM_102_ARAEAQQE_FAAN.pdf",
            mime="Doc/pdf",
            use_container_width=True
          )
    if Pump == 'MATRIX/A 5-6T':
        Co4= 1300
        V4= 2850
        Q4= 7.8
        H4 = 26.4
        Pt4 = 10
        P4 = float("{:.2f}".format((H4*9.8*1000)/100000))
        D4 = pd.DataFrame({
        'Consumo (Watts)': [Co4],
        'Velocidad (RPM)': [V4],
        'Caudal (m3/h)': [Q4],
        'Altura (m)': [H4],
        'P. trabajo @-22/55 ºC (Bar)': [Pt4],
        'P. Descarga (Bar)': [P4]
        })
        st.dataframe(D4, hide_index=True, use_container_width=True)
        with open("MATRIX.pdf", "rb") as file:
            btn = st.download_button(
            label="Ficha Técnica",
            data=file,
            file_name="MATRIX.pdf",
            mime="Doc/pdf",
            use_container_width=True
          )
    col4,col5,col6,col7 = st.columns(4)
    with col4:
        Vr = st.number_input("Volumen del recipiente (Litros)", value=None)
    with col5:
        Qc = st.number_input("Caudal de consumo en producción (m3/h)", value=None)
    with col6:
        if Pump == None:
            Qr = st.number_input("Caudal de recirculación (m3/h)", value=None)
        elif Pump == 'CM 3-5':
            Qr = st.number_input("Caudal de recirculación (m3/h)", value=Q1)
        elif Pump == 'CM 10-1':
            Qr = st.number_input("Caudal de recirculación (m3/h)", value=Q2)
        elif Pump == 'CM 10-2':
            Qr = st.number_input("Caudal de recirculación (m3/h)", value=Q3)
        elif Pump == 'MATRIX/A 5-6T':
            Qr = st.number_input("Caudal de recirculación (m3/h)", value=Q4)
    with col7:
        C = st.number_input("Concentración objetivo de Ozono Disuelto (PPM)", value=None)
    calcule = st.button("Calcular",use_container_width=True)
    st.divider()
    st.image("https://i.imgur.com/cQ1fWXQ.jpg")
#Parameters Calcule
    
    if calcule == True:
        st.divider()
        st.markdown("<h3 style='text-align: center;'>Resultados</h3>", unsafe_allow_html=True)
        col8,col9,col10 = st.columns(3)
        with col8:
            st.markdown("<p style='text-align: center;'>Tiempo de tratamiento completo vaso principal (min)</p>", unsafe_allow_html=True)
            Tt = float("{:.2f}".format(Qc/(Vr/1000)))
            st.markdown("<p style='text-align: center;'>{}</p>".format(str(Tt)), unsafe_allow_html=True)
        with col9:
            st.markdown("<p style='text-align: center;'>Tiempo de recirculacion en tanque (h)</p>", unsafe_allow_html=True)
            Tr = float("{:.2f}".format((Vr/1000)/Qr))
            st.markdown("<p style='text-align: center;'>{}</p>".format(str(Tr)), unsafe_allow_html=True) 
        with col10:
            st.markdown("<p style='text-align: center;'>Producción mínima esperada (g/h)</p>", unsafe_allow_html=True)
            Pe = float("{:.2f}".format((C*Qc)))
            st.markdown("<p style='text-align: center;'>{}</p>".format(str(Pe)), unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color:green'>Producción requerida (g/h)</3>", unsafe_allow_html=True)
        Pr = float("{:.2f}".format((1.5*Pe)/(0.8*0.9)))
        st.markdown("<h3 style='text-align: center; color:green'>{}</h3>".format(str(Pr)), unsafe_allow_html=True)
        



st.write("----------------------------------------------------------------------------------------------------")

st.markdown("<p style='text-align: center; color:gray; font-size: 14px;'> © 2024 PID Medioambiental, S.L. <br> J. Aguilar <br> Rev. 1.01 </p>", unsafe_allow_html=True)


