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

st.image("https://i.imgur.com/NwOV7Ob.jpg")

#Selecting the calcule for Ozone gas or water
option=st.selectbox('Tipo de instalación:', ('Ozono Agua','Ozono Aire'), index=None)

#OZONE IN WATER CALCULE
if option == "Ozono Agua":
    optionw=st.selectbox('Tipo de instalación:', ('Agua Potable','Aguas Residuales'), index=None)

    st.markdown("<h3 style='text-align: center;'>Parámetros de diseño</h3>", unsafe_allow_html=True)
    Pump=st.selectbox('Bomba de recirculación:', ('CM 3-5', 'CM 5-7', 'CM 10-1', 'CM 10-2', 'MATRIX/A 5-6T'), index=None)
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
    if Pump == 'CM 5-7':
        Co5= 1500
        V5= 2900
        Q5= 4.7
        H5 = 54.46
        Pt5= 10
        P5 = float("{:.2f}".format((H5*9.8*1000)/100000))
        D5 = pd.DataFrame({
        'Consumo (Watts)': [Co5],
        'Velocidad (RPM)': [V5],
        'Caudal (m3/h)': [Q5],
        'Altura (m)': [H5],
        'P. trabajo @-22/55 ºC (Bar)': [Pt5],
        'P. Descarga (Bar)': [P5]
        })
        st.dataframe(D5, hide_index=True, use_container_width=True)
        with open("98645137_CM_57_ARAEAVBE_FAAN.pdf", "rb") as file:
            btn = st.download_button(
            label="Ficha Técnica",
            data=file,
            file_name="98645137_CM_57_ARAEAVBE_FAAN.pdf",
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
    if Pump != None:
        Np = st.number_input("Cantidad de bombas (Solo en paralelo)", value=1)
    
    col4,col5,col6,col7 = st.columns(4)
    with col4:
        Vr = st.number_input("Volumen del recipiente (Litros)", value=None)
    with col5:
        Qc = st.number_input("Caudal de consumo en producción (m3/h)", value=None)
    with col6:
        if Pump == None:
            Qr = st.number_input("Caudal de recirculación (m3/h)", value=None)
        elif Pump == 'CM 3-5':
            Qr = st.number_input("Caudal de recirculación (m3/h)", value=Q1*Np)
        elif Pump == 'CM 5-7':
            Qr = st.number_input("Caudal de recirculación (m3/h)", value=Q5*Np)
        elif Pump == 'CM 10-1':
            Qr = st.number_input("Caudal de recirculación (m3/h)", value=Q2*Np)
        elif Pump == 'CM 10-2':
            Qr = st.number_input("Caudal de recirculación (m3/h)", value=Q3*Np)
        elif Pump == 'MATRIX/A 5-6T':
            Qr = st.number_input("Caudal de recirculación (m3/h)", value=Q4*Np)
    with col7:
        C = st.number_input("Concentración objetivo de Ozono Disuelto (PPM)", value=None)

    if optionw == "Agua Potable":
        st.divider()
        st.markdown("<h3 style='text-align: center;'>Factores de diseño</h3>", unsafe_allow_html=True)
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
      
    if optionw == "Aguas Residuales":
        st.divider()
        st.markdown("<h3 style='text-align: center;'>Contaminantes</h3>", unsafe_allow_html=True)
        col104,col105,col106,col107 = st.columns(4)
        with col104:
            Fe = st.number_input("Fe (g/m3)", value=0.00)
            Fes = 0.44
        with col105:
            Mn = st.number_input("Mn (g/m3)", value=0.00)
            Mns = 0.88
        with col106:
            DQO = st.number_input("DQO (g/m3)", value=0.00)
            DQOs=1.5
        with col107:
            DBO = st.number_input("DBO (g/m3)", value=0.00)
            DBOs=1.5

        Cm= float("{:.2f}".format((Fe*Fes+Mn*Mns+DQO*DQOs+DBO*DBOs)*Qc))
    
        st.markdown("<h3 style='text-align: center;'>Factores de diseño</h3>", unsafe_allow_html=True)
        col1,col2,col3,cole = st.columns(4)
        with col1:
            st.markdown("<p style='text-align: center;'>Factor de seguridad por transferencia de masa</p>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>0.9</p>", unsafe_allow_html=True)
        with col2:
            st.markdown("<p style='text-align: center;'>Factor de seguridad por rendimiento de generación</p>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>0.8</p>", unsafe_allow_html=True)
        with col3:
            st.markdown("<p style='text-align: center;'>Factor de seguridad general de diseño</p>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>1.5</p>", unsafe_allow_html=True)
        with cole:
            st.markdown("<p style='text-align: center;'>Elementos Contaminantes (gr/h)</p>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>{}</p>".format(str(Cm)), unsafe_allow_html=True)            

    calcule = st.button("Calcular",use_container_width=True)
    
    #Parameters Calcule
    if optionw == 'Agua Potable' and calcule == True:
        if Vr is None:
            st.error("❌ Debes introducir un volumen antes de calcular.")
            st.stop()
        if Qr is None:
            st.error("❌ Debes introducir un Caudal de Recirculación antes de calcular.")
            st.stop()
        if Qc is None:
            st.error("❌ Debes introducir un Caudal de Consumo antes de calcular.")
            st.stop()
        if C is None:
            st.error("❌ Debes introducir una concentración objetivo antes de calcular.")
            st.stop()
        st.divider()
        st.markdown("<h3 style='text-align: center;'>Resultados</h3>", unsafe_allow_html=True)
        col8,col9,col10 = st.columns(3)
        with col8:
            st.markdown("<p style='text-align: center;'>Tiempo de tratamiento completo vaso principal (min)</p>", unsafe_allow_html=True)
            Tt = float("{:.2f}".format((((Vr/1000)/Qc)*60*1.25))) #Security Factor 25%
            st.markdown("<p style='text-align: center;'>{}</p>".format(str(Tt)), unsafe_allow_html=True)
        with col9:
            st.markdown("<p style='text-align: center;'>Tiempo de recirculacion en tanque (min)</p>", unsafe_allow_html=True)
            Tr = float("{:.2f}".format(((Vr/1000)/Qr)*60))
            st.markdown("<p style='text-align: center;'>{}</p>".format(str(Tr)), unsafe_allow_html=True) 
        with col10:
            st.markdown("<p style='text-align: center;'>Producción mínima esperada (g/h)</p>", unsafe_allow_html=True)
            Pe = float("{:.2f}".format((C*Qc)))
            st.markdown("<p style='text-align: center;'>{}</p>".format(str(Pe)), unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color:green'>Producción requerida (g/h)</3>", unsafe_allow_html=True)
        Pr = float("{:.2f}".format((1.5*Pe)/(0.8*0.9)))
        st.markdown("<h3 style='text-align: center; color:green'>{}</h3>".format(str(Pr)), unsafe_allow_html=True)
        st.divider()
    elif optionw == 'Aguas Residuales' and calcule == True:
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
        Pr = float("{:.2f}".format(((1.5*Pe)/(0.8*0.9))+Cm))
        st.markdown("<h3 style='text-align: center; color:green'>{}</h3>".format(str(Pr)), unsafe_allow_html=True)
        st.divider()
    
    if calcule == True:
        # --- Tabla con todos los sistemas y sus rangos ---
        sistemas = [
        # Pr <= 2
        {"min": 0, "max": 2, "modelo": "ZHI1250", "gas": "Aire", "caudal": "8 L/min",
        "original": "0.01 gr/h", "nominal": "0.01 gr/h", "pdf": "TDS Z-ZHI ES TTO Biocida 2024 (1250).pdf",
        "imagen": ""},     
        {"min": 0, "max": 2, "modelo": "ZHI3000", "gas": "Aire", "caudal": "8 L/min",
        "original": "0.03 gr/h", "nominal": "0.03 gr/h", "pdf": "TDS Z-ZHI ES TTO Biocida 2024 (3000).pdf",
        "imagen": ""},        
        {"min": 0, "max": 2, "modelo": "ZHI6000", "gas": "Aire", "caudal": "8 L/min",
        "original": "0.06 gr/h", "nominal": "0.06 gr/h", "pdf": "TDS Z-ZHI ES TTO Biocida 2024 (6000).pdf",
        "imagen": ""},        
        {"min": 0, "max": 2, "modelo": "ZHI10000", "gas": "Aire", "caudal": "8 L/min",
        "original": "0.08 gr/h", "nominal": "0.08 gr/h", "pdf": "TDS Z-ZHI ES TTO Biocida 2024 (10000).pdf",
        "imagen": ""},       
        {"min": 0, "max": 2, "modelo": "ZHI300MG", "gas": "Aire", "caudal": "8 L/min",
        "original": "0.29 gr/h", "nominal": "0.29 gr/h", "pdf": "TDS Z-ZHI ES TTO Biocida 2024 (300mg).pdf",
        "imagen": ""},        
        {"min": 0, "max": 2, "modelo": "ZHI500MG", "gas": "Aire", "caudal": "8 L/min",
        "original": "0.32 gr/h", "nominal": "0.32 gr/h", "pdf": "TDS Z-ZHI ES TTO Biocida 2024 (500mg).pdf",
        "imagen": ""},        
        {"min": 0, "max": 2, "modelo": "ZHI1000MG", "gas": "Aire", "caudal": "8 L/min",
        "original": "0.57 gr/h", "nominal": "0.57 gr/h", "pdf": "TDS Z-ZHI ES TTO Biocida 2024 (1000mg).pdf",
        "imagen": ""},      
        {"min": 0, "max": 2, "modelo": "SP Mini 300MG", "gas": "Aire", "caudal": "8 L/min",
        "original": "0.29 gr/h", "nominal": "0.29 gr/h", "pdf": "TDS SP MINI ES TTO Biocida 2024 (300mg).pdf",
        "imagen": ""},   
        {"min": 0, "max": 2, "modelo": "SP Mini 500MG", "gas": "Aire", "caudal": "8 L/min",
        "original": "0.34 gr/h", "nominal": "0.34 gr/h", "pdf": "TDS SP MINI ES TTO Biocida 2024 (500mg).pdf",
        "imagen": ""},    
        {"min": 0, "max": 2, "modelo": "SP Mini 1g", "gas": "Aire", "caudal": "8 L/min",
        "original": "0.57 gr/h", "nominal": "0.57 gr/h", "pdf": "TDS SP MINI ES TTO Biocida 2024 (1g).pdf",
        "imagen": ""},    
        {"min": 0, "max": 2, "modelo": "SP Mini 2g", "gas": "Aire", "caudal": "8 L/min",
        "original": "0.94 gr/h", "nominal": "0.94 gr/h", "pdf": "TDS SP MINI ES TTO Biocida 2024 (2g).pdf",
        "imagen": ""},    
        {"min": 0, "max": 2, "modelo": "SP 300MG", "gas": "Aire", "caudal": "8 L/min",
        "original": "0.27 gr/h", "nominal": "0.27 gr/h", "pdf": "TDS SP ES TTO Biocida 2024 (300mg).pdf",
        "imagen": ""},   
        {"min": 0, "max": 2, "modelo": "SP 500MG", "gas": "Aire", "caudal": "8 L/min",
        "original": "0.34 gr/h", "nominal": "0.34 gr/h", "pdf": "TDS SP ES TTO Biocida 2024 (500mg).pdf",
        "imagen": ""},    
        {"min": 0, "max": 2, "modelo": "SP 1g", "gas": "Aire", "caudal": "8 L/min",
        "original": "0.41 gr/h", "nominal": "0.41 gr/h", "pdf": "TDS SP ES TTO Biocida 2024 (1g).pdf",
        "imagen": ""},    
  

        # 2 < Pr <= 4
        {"min": 2, "max": 4, "modelo": "SP-24", "gas": "Oxígeno @90-94%", "caudal": "1 L/min",
        "original": "5 gr/h", "nominal": "3.96 gr/h", "pdf": "Ficha tecnica SP 24 v3.pdf",
        "imagen": "https://i.imgur.com/mcAZEg0.jpg"},

        # 4 < Pr <= 7
        {"min": 4, "max": 7, "modelo": "SP-21 20", "gas": "Oxígeno @90-94%", "caudal": "1.5 L/min",
        "original": "20 gr/h", "nominal": "6.63 gr/h", "pdf": "Ficha Técnica SP21.pdf",
        "imagen": "https://i.imgur.com/jVRU4mY.jpg"},        
        {"min": 4, "max": 7, "modelo": "SP-5 Oxi 20", "gas": "Oxígeno @90-94%", "caudal": "1.5 L/min",
        "original": "—", "nominal": "6.63 gr/h", "pdf": "Ficha Técnica SP5 oxi.pdf",
        "imagen": "https://i.imgur.com/j4Ujngv.jpg"},
 
        # 7 < Pr <= 12
        {"min": 7, "max": 12, "modelo": "SP-5 Oxi 30", "gas": "Oxígeno @90-94%", "caudal": "1.5 L/min",
        "original": "30 gr/h", "nominal": "8.49 gr/h", "pdf": "Ficha Técnica SP5 oxi.pdf",
        "imagen": "https://i.imgur.com/j4Ujngv.jpg"},
        {"min": 7, "max": 12, "modelo": "SP-21 40", "gas": "Oxígeno @90-94%", "caudal": "10 L/min",
        "original": "40 gr/h", "nominal": "8.49 gr/h", "pdf": "Ficha Técnica SP21.pdf",
        "imagen": "https://i.imgur.com/jVRU4mY.jpg"},

        # 12 < Pr <= 20

        # 20 < Pr <= 45
        {"min": 20, "max": 45, "modelo": "SP-22", "gas": "Oxígeno @90-94%", "caudal": "10 L/min",
        "original": "40 gr/h", "nominal": "31.65 gr/h", "pdf": "Ficha Técnica SP22.pdf",
        "imagen": "https://i.imgur.com/fA7a6Sn.jpg"},
        {"min": 20, "max": 45, "modelo": "SP-23", "gas": "Oxígeno @90-94%", "caudal": "10 L/min",
        "original": "80 gr/h", "nominal": "40.16 gr/h",
        "pdf": "Ficha tecnica SP 23 Clientes Rev 3 Industrial sanidad.pdf",
        "imagen": "https://i.imgur.com/6zK69Kq.jpg"},
        {"min": 20, "max": 45, "modelo": "SP-25", "gas": "Oxígeno @90-94%", "caudal": "10 L/min",
        "original": "40 gr/h", "nominal": "31.65 gr/h", "pdf": "Ficha tecnica SP 25.pdf",
        "imagen": "https://i.imgur.com/OI3WF8q.jpg"},
        {"min": 20, "max": 45, "modelo": "SP-5 20 gr", "gas": "Oxígeno @90-94%", "caudal": "10 L/min",
        "original": "20 gr/h", "nominal": "20.42 gr/h", "pdf": "Ficha Técnica SP520.pdf",
        "imagen": "https://i.imgur.com/j4Ujngv.jpg"},
        {"min": 20, "max": 45, "modelo": "SP-5 30", "gas": "Oxígeno @90-94%", "caudal": "10 L/min",
        "original": "60 gr/h", "nominal": "31.65 gr/h", "pdf": "Ficha Técnica SP530.pdf",
        "imagen": "https://i.imgur.com/gpKw594.jpg"},
        {"min": 20, "max": 45, "modelo": "SP-5 45", "gas": "Oxígeno @90-94%", "caudal": "10 L/min",
        "original": "60 gr/h", "nominal": "42.66 gr/h", "pdf": "Ficha Técnica SP545.pdf",
        "imagen": "https://i.imgur.com/gpKw594.jpg"},
        {"min": 20, "max": 45, "modelo": "SP-5 60", "gas": "Oxígeno @90-94%", "caudal": "10 L/min",
        "original": "60 gr/h", "nominal": "42.66 gr/h", "pdf": "Ficha Técnica SP560.pdf",
        "imagen": "https://i.imgur.com/gpKw594.jpg"},
        {"min": 20, "max": 45, "modelo": "SP-20 60 gr", "gas": "Oxígeno @90-94%", "caudal": "10 L/min",
        "original": "60 gr/h", "nominal": "42.66 gr/h", "pdf": "Ficha Técnica SP 20.pdf",
        "imagen": "https://i.imgur.com/cJRniPE.jpg"},
    ]

    # --- Mostrar recomendaciones ---
    if calcule:
        st.markdown("<h3 style='text-align: center;'>Sistemas Recomendados</h3>", unsafe_allow_html=True)

        # Filtrar por rango
        recomendados = [s for s in sistemas if s["min"] <= Pr <= s["max"]]

        # Si no hay coincidencias y Pr > 20, mostrar nota
        if Pr > 50:
            st.markdown("<h4 style='text-align: center;'>NOTA: Para concentraciones mayores a 50 gr/h considere la combinación de 2 o más sistemas</h4>", unsafe_allow_html=True)
            recomendados = [s for s in sistemas if s["max"] == 50]  # mostrar los más potentes

        if not recomendados:
            st.info("No se encontraron sistemas recomendados para este valor de Pr.")
        else:
            # Mostrar los sistemas en pares de columnas
            for i in range(0, len(recomendados), 2):
                cols = st.columns(2)
                for col, sistema in zip(cols, recomendados[i:i+2]):
                    with col:
                        st.markdown(f"<h4 style='text-align: center;'>{sistema['modelo']}</h4>", unsafe_allow_html=True)
                        st.markdown(
                            f"<p style='text-align: center;'>"
                            f"Gas de alimentación: {sistema['gas']} <br>"
                            f"Caudal Gas: {sistema['caudal']} <br>"
                            f"Capacidad Nominal: {sistema['nominal']}</p>",
                            unsafe_allow_html=True
                        )
                        with open(sistema["pdf"], "rb") as file:
                            st.download_button(
                                label="Ficha Técnica",
                                data=file,
                                file_name=sistema["pdf"],
                                mime="Doc/pdf",
                                use_container_width=True
                            )
                            
                
    st.divider()
    st.markdown("<h3 style='text-align: center;'>Curvas de desinfección del Agua: Concentración vs. Redox", unsafe_allow_html=True)
    st.image("https://i.imgur.com/cQ1fWXQ.jpg")


#OZONE IN AIR CALCULE
if option == "Ozono Aire":
    optiona = st.selectbox('Seleccione el Generador:', ('Calculo sin generador asignado','Z1250T','Z3000T','Z6000T','Z10000T','Z20000T','ZHI1250','ZHI3000',
                                                                      'ZHI6000','ZHI10000','ZHI300MG','ZHI500MG','ZHI1000MG','Cañon 5','Cañon 12',
                                                                      'SP Mini 300mg','SP Mini 500mg','SP Mini 1g','SP Mini 2g','SP 300mg',
                                                                      'SP 500mg','SP 1g','SP 2g','SP 4g','SP 8g','SP 10g','SP 15g','SP5 20',
                                                                      'SP5 30','SP5 45','SP5 60','SP21 20','SP21 40','SP5 Oxi 20','SP5 Oxi 30',
                                                                      'SP18','SP20A'), index=None)
    
    if optiona == 'Calculo sin generador asignado' or optiona == None:
        SelectedQg=None
    elif optiona in ['Z1250T','Z3000T','Z6000T','Z10000T','Z20000T']:
        SelectedQg=518
    elif optiona in ['ZHI1250','ZHI3000', 'ZHI6000','ZHI10000','ZHI300MG','ZHI500MG','ZHI1000MG','SP Mini 300mg','SP Mini 500mg','SP Mini 1g','SP Mini 2g']:
        SelectedQg=8
    elif optiona in ['Cañon 5','Cañon 12']:
        SelectedQg=3333
    elif optiona in ['SP 300mg','SP 500mg','SP 1g','SP 2g','SP 4g','SP 8g','SP 10g','SP 15g']:
        SelectedQg=30
    elif optiona in ['SP5 20','SP5 30','SP5 45','SP5 60','SP18','SP20A'] :
        SelectedQg=10
    elif optiona in ['SP21 20','SP21 40','SP5 Oxi 20','SP5 Oxi 30']:
        SelectedQg=1.5

    if optiona == 'Calculo sin generador asignado' or optiona == None:
        SelectedPr=None
    elif optiona == 'Z1250T':
        SelectedPr=0.02
    elif optiona == 'Z3000T':
        SelectedPr=0.03
    elif optiona == 'Z6000T':
        SelectedPr=0.07
    elif optiona == 'Z10000T':
        SelectedPr=0.08
    elif optiona == 'Z20000T':
        SelectedPr=0.10
    elif optiona == 'ZHI1250':
        SelectedPr=0.01
    elif optiona == 'ZHI3000':
        SelectedPr=0.03
    elif optiona == 'ZHI6000':
        SelectedPr=0.06
    elif optiona == 'ZHI10000':
        SelectedPr=0.08
    elif optiona == 'ZHI300MG':
        SelectedPr=0.29
    elif optiona == 'ZHI500MG':
        SelectedPr=0.32
    elif optiona == 'ZHI1000MG':
        SelectedPr=0.57
    elif optiona == 'Cañon 5':
        SelectedPr=4
    elif optiona == 'Cañon 12':
        SelectedPr=10.60
    elif optiona == 'SP Mini 300mg':
        SelectedPr=0.29
    elif optiona == 'SP Mini 500mg':
        SelectedPr=0.32
    elif optiona == 'SP Mini 1g':
        SelectedPr=0.57
    elif optiona == 'SP Mini 2g':
        SelectedPr=0.94
    elif optiona == 'SP 300mg':
        SelectedPr=0.27
    elif optiona == 'SP 500mg':
        SelectedPr=0.34
    elif optiona == 'SP 1g':
        SelectedPr=0.41
    elif optiona == 'SP 2g':
        SelectedPr=3.24
    elif optiona == 'SP 4g':
        SelectedPr=3.94
    elif optiona == 'SP 8g':
        SelectedPr=4.62
    elif optiona == 'SP 10g':
        SelectedPr=6.38
    elif optiona == 'SP 15g':
        SelectedPr=4.48
    elif optiona == 'SP5 20':
        SelectedPr=20.42
    elif optiona == 'SP5 30':
        SelectedPr=31.65
    elif optiona == 'SP5 45':
        SelectedPr=42.66
    elif optiona == 'SP5 60':
        SelectedPr=42.66
    elif optiona == 'SP21 20':
        SelectedPr=6.63
    elif optiona == 'SP21 40':
        SelectedPr=8.49
    elif optiona == 'SP5 Oxi 20':
        SelectedPr=6.63
    elif optiona == 'SP5 Oxi 30':
        SelectedPr=8.49
    elif optiona == 'SP18':
        SelectedPr=42.66
    elif optiona == 'SP20A':
        SelectedPr=42.66
    
    Qg = SelectedQg
    Pr = SelectedPr

    if optiona != None:
        Vei = st.number_input("Volumen del espacio a tratar", value=None)
        option_map ={
            0:'Metros cúbicos (m3)',
            1: 'Litros (L)',
        }
        airUnitSelection = st.pills('Unidad', options=option_map.keys(),format_func=lambda option: option_map[option],selection_mode="single",)
        if airUnitSelection == 0:
            Ve = Vei*1000
        elif airUnitSelection == 1:
            Ve = Vei

    if optiona == 'Calculo sin generador asignado' and Vei != None:
        st.divider()
        col19,col20= st.columns(2)
        with col19:
            if optiona == None:
                Qg = st.number_input("Caudal de salida del gas (L/min)", value=None)
            else:
                Qg = st.number_input("Caudal de salida del gas (L/min)", value= SelectedQg)

        with col20:
            if optiona == None:
                Pr = st.number_input("Producción seleccionada (g/h)", value=None)
            else:
                Pr = st.number_input("Producción seleccionada (g/h)", value= SelectedPr)

    col1,col2,col3 = st.columns(3)
    with col1:
        st.markdown("<p style='text-align: center;'>Concentración (g/m3)</p>", unsafe_allow_html=True)
        if Pr == None:
            Co = 0
        else:
            Co=float("{:.4f}".format((Pr/(Qg*60))*1000))
        st.markdown("<p style='text-align: center;'>{}</p>".format(str(Co)), unsafe_allow_html=True)
    with col2:
        st.markdown("<p style='text-align: center;'>Constante K</p>", unsafe_allow_html=True)
        k = 1.65
        st.markdown("<p style='text-align: center;'>{}</p>".format(str(k)), unsafe_allow_html=True)
    with col3:
        fi = st.slider("Factor de Intercambio", min_value=0.5, max_value=1.2, value=0.8)
        
    calcule = st.button("Calcular",use_container_width=True)

    if calcule == True:
        if airUnitSelection is None:
            st.error("❌ Debes seleccionar la unidad de Volumen antes de calcular.")
            st.stop()
        if Vei is None:
            st.error("❌ Debes introducir un Volumen antes de calcular.")
            st.stop()
        if Qg is None:
            st.error("❌ Debes introducir un Valor de caudal antes de calcular.")
            st.stop()
        if Pr is None:
            st.error("❌ Debes introducir un Valor de producción antes de calcular.")
            st.stop()
        st.markdown("<h3 style='text-align: center;'>Resultados</h3>", unsafe_allow_html=True)
        #Variables of air ozone
        c0=0
        ppm0=0
        c1=(c0+0.1*(-k*c0+((Qg*60)/Ve)*((Co/1000)-c0)-fi*((Qg*60)/Ve)*c0))
        ppm1=c1*(1000000*0.51)
        c2=(c1+0.1*(-k*c1+((Qg*60)/Ve)*((Co/1000)-c1)-fi*((Qg*60)/Ve)*c1))
        ppm2=c2*(1000000*0.51)
        c3=(c2+0.1*(-k*c2+((Qg*60)/Ve)*((Co/1000)-c2)-fi*((Qg*60)/Ve)*c2))
        ppm3=c3*(1000000*0.51)
        c4=(c3+0.1*(-k*c3+((Qg*60)/Ve)*((Co/1000)-c3)-fi*((Qg*60)/Ve)*c3))
        ppm4=c4*(1000000*0.51)
        c5=(c4+0.1*(-k*c4+((Qg*60)/Ve)*((Co/1000)-c4)-fi*((Qg*60)/Ve)*c4))
        ppm5=c5*(1000000*0.51)
        c6=(c5+0.1*(-k*c5+((Qg*60)/Ve)*((Co/1000)-c5)-fi*((Qg*60)/Ve)*c5))
        ppm6=c6*(1000000*0.51)
        c7=(c6+0.1*(-k*c6+((Qg*60)/Ve)*((Co/1000)-c6)-fi*((Qg*60)/Ve)*c6))
        ppm7=c7*(1000000*0.51)
        c8=(c7+0.1*(-k*c7+((Qg*60)/Ve)*((Co/1000)-c7)-fi*((Qg*60)/Ve)*c7))
        ppm8=c8*(1000000*0.51)
        c9=(c8+0.1*(-k*c8+((Qg*60)/Ve)*((Co/1000)-c8)-fi*((Qg*60)/Ve)*c8))
        ppm9=c9*(1000000*0.51)
        c10=(c9+0.1*(-k*c9+((Qg*60)/Ve)*((Co/1000)-c9)-fi*((Qg*60)/Ve)*c9))
        ppm10=c10*(1000000*0.51)
        c11=(c10+0.1*(-k*c10+((Qg*60)/Ve)*((Co/1000)-c10)-fi*((Qg*60)/Ve)*c10))
        ppm11=c11*(1000000*0.51)
        c12=(c11+0.1*(-k*c11+((Qg*60)/Ve)*((Co/1000)-c11)-fi*((Qg*60)/Ve)*c11))
        ppm12=c12*(1000000*0.51)
        c13=(c12+0.1*(-k*c12+((Qg*60)/Ve)*((Co/1000)-c12)-fi*((Qg*60)/Ve)*c12))
        ppm13=c13*(1000000*0.51)
        c14=(c13+0.1*(-k*c13+((Qg*60)/Ve)*((Co/1000)-c13)-fi*((Qg*60)/Ve)*c13))
        ppm14=c14*(1000000*0.51)
        c15=(c14+0.1*(-k*c14+((Qg*60)/Ve)*((Co/1000)-c14)-fi*((Qg*60)/Ve)*c14))
        ppm15=c15*(1000000*0.51)
        c16=(c15+0.1*(-k*c15+((Qg*60)/Ve)*((Co/1000)-c15)-fi*((Qg*60)/Ve)*c15))
        ppm16=c16*(1000000*0.51)
        c17=(c16+0.1*(-k*c16+((Qg*60)/Ve)*((Co/1000)-c16)-fi*((Qg*60)/Ve)*c16))
        ppm17=c17*(1000000*0.51)
        c18=(c17+0.1*(-k*c17+((Qg*60)/Ve)*((Co/1000)-c17)-fi*((Qg*60)/Ve)*c17))
        ppm18=c18*(1000000*0.51)
        c19=(c18+0.1*(-k*c18+((Qg*60)/Ve)*((Co/1000)-c18)-fi*((Qg*60)/Ve)*c18))
        ppm19=c19*(1000000*0.51)
        c20=(c19+0.1*(-k*c19+((Qg*60)/Ve)*((Co/1000)-c19)-fi*((Qg*60)/Ve)*c19))
        ppm20=c20*(1000000*0.51)
        c21=(c20+0.1*(-k*c20+((Qg*60)/Ve)*((Co/1000)-c20)-fi*((Qg*60)/Ve)*c20))
        ppm21=c21*(1000000*0.51)
        c22=(c21+0.1*(-k*c21+((Qg*60)/Ve)*((Co/1000)-c21)-fi*((Qg*60)/Ve)*c21))
        ppm22=c22*(1000000*0.51)
        c23=(c22+0.1*(-k*c22+((Qg*60)/Ve)*((Co/1000)-c22)-fi*((Qg*60)/Ve)*c22))
        ppm23=c23*(1000000*0.51)
        c24=(c23+0.1*(-k*c23+((Qg*60)/Ve)*((Co/1000)-c23)-fi*((Qg*60)/Ve)*c23))
        ppm24=c24*(1000000*0.51)
        c25=(c24+0.1*(-k*c24+((Qg*60)/Ve)*((Co/1000)-c24)-fi*((Qg*60)/Ve)*c24))
        ppm25=c25*(1000000*0.51)
        c26=(c25+0.1*(-k*c25+((Qg*60)/Ve)*((Co/1000)-c25)-fi*((Qg*60)/Ve)*c25))
        ppm26=c26*(1000000*0.51)
        c27=(c26+0.1*(-k*c26+((Qg*60)/Ve)*((Co/1000)-c26)-fi*((Qg*60)/Ve)*c26))
        ppm27=c27*(1000000*0.51)
        c28=(c27+0.1*(-k*c27+((Qg*60)/Ve)*((Co/1000)-c27)-fi*((Qg*60)/Ve)*c27))
        ppm28=c28*(1000000*0.51)
        c29=(c28+0.1*(-k*c28+((Qg*60)/Ve)*((Co/1000)-c28)-fi*((Qg*60)/Ve)*c28))
        ppm29=c29*(1000000*0.51)
        c30=(c29+0.1*(-k*c29+((Qg*60)/Ve)*((Co/1000)-c29)-fi*((Qg*60)/Ve)*c29))
        ppm30=c30*(1000000*0.51)    
        c31=(c30+0.1*(-k*c30+((Qg*60)/Ve)*((Co/1000)-c30)-fi*((Qg*60)/Ve)*c30))
        ppm31=c31*(1000000*0.51)
        c32=(c31+0.1*(-k*c31+((Qg*60)/Ve)*((Co/1000)-c31)-fi*((Qg*60)/Ve)*c31))
        ppm32=c32*(1000000*0.51)
        c33=(c32+0.1*(-k*c32+((Qg*60)/Ve)*((Co/1000)-c32)-fi*((Qg*60)/Ve)*c32))
        ppm33=c33*(1000000*0.51)
        c34=(c33+0.1*(-k*c33+((Qg*60)/Ve)*((Co/1000)-c33)-fi*((Qg*60)/Ve)*c33))
        ppm34=c34*(1000000*0.51)
        c35=(c34+0.1*(-k*c34+((Qg*60)/Ve)*((Co/1000)-c34)-fi*((Qg*60)/Ve)*c34))
        ppm35=c35*(1000000*0.51)

        D3=pd.DataFrame({
        'Tiempo (min)': [0,6,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96,102,108,114,120,126,132,138,144,150,156,162,168,174,180,186,192,198,204],
        'Concentración (A)': [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,c30,c31,c32,c33,c34,c35],
        'Concentración O3 (PPM)': [ppm0,ppm1,ppm2,ppm3,ppm4,ppm5,ppm6,ppm7,ppm8,ppm9,ppm10,ppm12,ppm13,ppm14,ppm15,ppm16,ppm17,ppm18,ppm19,ppm20,ppm21,ppm22,ppm23,ppm24,ppm25,ppm26,ppm27,ppm28,ppm29,ppm30,ppm31,ppm32,ppm33,ppm34,ppm35]
        })
        st.dataframe(D3.style.format({'Concentración (A)':"{:.10}"}), hide_index=True, use_container_width=True, height=1260)
        st.line_chart(D3, x="Tiempo (min)", y="Concentración O3 (PPM)")

st.write("----------------------------------------------------------------------------------------------------")

st.markdown("<p style='text-align: center; color:gray; font-size: 14px;'> © 2024 PID Medioambiental, S.L. <br> J. Aguilar & G. Balanguero <br> Rev. 1.01 </p>", unsafe_allow_html=True)


