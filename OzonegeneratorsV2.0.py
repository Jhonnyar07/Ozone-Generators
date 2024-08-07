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
    
    def sp520():
        col13,col14 = st.columns(2)
        with col13:
            st.markdown("<h4 style='text-align: center;'>SP-5 20 gr</h4>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Composición: 1 Celda OC15</p>", unsafe_allow_html=True)
            DSP520 = pd.DataFrame({
            'Caudal O2 (l/min)': [1,2,3,4,5,6,7,8,9],
            'Conc. O3 (gr/m3)': [75,69,67,62,58,48,43,40,37],
            'Prod. O3 (g/h)': [4.5,8.28,12.06,14.88,17.4,17.28,18.06,19.2,19.98]
            })
            st.dataframe(DSP520, hide_index=True, use_container_width=True)
            with open("Ficha Técnica SP5.pdf", "rb") as file:
                btn1 = st.download_button(
                label="Ficha Técnica",
                data=file,
                file_name="Ficha Técnica SP520.pdf",
                mime="Doc/pdf",
                use_container_width=True
                )        
        with col14:
            st.image('https://i.imgur.com/j4Ujngv.jpg')

    def sp545():
        col13,col14 = st.columns(2)
        with col13:
            st.markdown("<h4 style='text-align: center;'>SP-5 45 gr</h4>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Composición: 2 Celdas OC15 en serie</p>", unsafe_allow_html=True)
            DSP545 = pd.DataFrame({
            'Caudal O2 (l/min)': [1,2,3,4,5,6,7,8,9],
            'Conc. O3 (gr/m3)': [70,71,72,70,67,60,59,56,52],
            'Prod. O3 (g/h)': [4.2,8.52,12.96,16.8,20.1,21.6,24.78,26.88,28.08]
            })
            st.dataframe(DSP545, hide_index=True, use_container_width=True)
            with open("Ficha Técnica SP5.pdf", "rb") as file:
                btn2 = st.download_button(
                label="Ficha Técnica",
                data=file,
                file_name="Ficha Técnica SP545g.pdf",
                mime="Doc/pdf",
                use_container_width=True
                )        
        with col14:
            st.image('https://i.imgur.com/j4Ujngv.jpg')
    
    def sp560():
        col13,col14 = st.columns(2)
        with col13:
            st.markdown("<h4 style='text-align: center;'>SP-5 60 gr</h4>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Composición: 3 Celdas OC15 en serie</p>", unsafe_allow_html=True)
            DSP560 = pd.DataFrame({
            'Caudal O2 (l/min)': [1,2,3,4,5,6,7,8,9],
            'Conc. O3 (gr/m3)': [60,67,70.2,72,71,63,57,50,43],
            'Prod. O3 (g/h)': [3.6,8.04,12.636,17.28,21.3,22.68,23.94,24,23.22]
            })
            st.dataframe(DSP560, hide_index=True, use_container_width=True)
            with open("Ficha Técnica SP5.pdf", "rb") as file:
                btn3 = st.download_button(
                label="Ficha Técnica",
                data=file,
                file_name="Ficha Técnica SP560g.pdf",
                mime="Doc/pdf",
                use_container_width=True
                )        
        with col14:
            st.image('https://i.imgur.com/j4Ujngv.jpg')
            
    def sp18():
        col20,col21 = st.columns(2)
        with col20:
            st.markdown("<h4 style='text-align: center;'>SP-18 60 gr</h4>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Composición: 3 Celdas OC15 en serie</p>", unsafe_allow_html=True)
            DSP18 = pd.DataFrame({
            'Caudal O2 (l/min)': [1,2,3,4,5,6,7,8,9],
            'Conc. O3 (gr/m3)': [60,67,70.2,72,71,63,57,50,43],
            'Prod. O3 (g/h)': [3.6,8.04,12.636,17.28,21.3,22.68,23.94,24,23.22]
            })
            st.dataframe(DSP18, hide_index=True, use_container_width=True)
            with open("Ficha Técnica SP18.pdf", "rb") as file:
                    btn4 = st.download_button(
                    label="Ficha Técnica",
                    data=file,
                    file_name="Ficha Técnica SP18.pdf",
                    mime="Doc/pdf",
                    use_container_width=True
                    )        
        with col21:
            st.image('https://i.imgur.com/gpKw594.jpg')

    def sp2060():
        col22,col23 = st.columns(2)
        with col22:
            st.markdown("<h4 style='text-align: center;'>SP-20 60 gr</h4>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Composición: 3 Celdas OC15 en serie</p>", unsafe_allow_html=True)
            DSP2060 = pd.DataFrame({
            'Caudal O2 (l/min)': [1,2,3,4,5,6,7,8,9],
            'Conc. O3 (gr/m3)': [60,67,70.2,72,71,63,57,50,43],
            'Prod. O3 (g/h)': [3.6,8.04,12.636,17.28,21.3,22.68,23.94,24,23.22]
            })
            st.dataframe(DSP2060, hide_index=True, use_container_width=True)
            with open("Ficha Técnica SP 20.pdf", "rb") as file:
                btn1 = st.download_button(
                label="Ficha Técnica",
                data=file,
                file_name="Ficha Técnica SP 20.pdf",
                mime="Doc/pdf",
                use_container_width=True
                )        
        with col23:
            st.image('https://i.imgur.com/cJRniPE.jpg')

    def sp2080():
        col22,col23 = st.columns(2)
        with col22:
            st.markdown("<h4 style='text-align: center;'>SP-20 80 gr</h4>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Composición: 4 Celdas OC15 en serie</p>", unsafe_allow_html=True)
            DSP2080 = pd.DataFrame({
            'Caudal O2 (l/min)': [1,2,3,4,5,6,7,8,9],
            'Conc. O3 (gr/m3)': [51,56,60,62,66,66,62,55,46],
            'Prod. O3 (g/h)': [3.06,6.72,10.8,14.88,19.8,23.76,26.04,26.4,24.84]
            })
            st.dataframe(DSP2080, hide_index=True, use_container_width=True)
            with open("Ficha Técnica SP 20.pdf", "rb") as file:
                btn1 = st.download_button(
                label="Ficha Técnica",
                data=file,
                file_name="Ficha Técnica SP 2080.pdf",
                mime="Doc/pdf",
                use_container_width=True
                )        
        with col23:
            st.image('https://i.imgur.com/cJRniPE.jpg')
    
    def sp23():
        col15,col16 = st.columns(2)
        with col15:
            st.markdown("<h4 style='text-align: center;'>SP-23 80 gr</h4>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Composición: 4 Celdas OC15 en serie</p>", unsafe_allow_html=True)
            DSP23 = pd.DataFrame({
            'Caudal O2 (l/min)': [1,2,3,4,5,6,7,8,9],
            'Conc. O3 (gr/m3)': [51,56,60,62,66,66,62,55,46],
            'Prod. O3 (g/h)': [3.06,6.72,10.8,14.88,19.8,23.76,26.04,26.4,24.84]
            })
            st.dataframe(DSP23, hide_index=True, use_container_width=True)
            with open("Ficha tecnica SP 23 Clientes Rev 3 Industrial sanidad.pdf", "rb") as file:
                btn3 = st.download_button(
                label="Ficha Técnica",
                data=file,
                file_name="Ficha tecnica SP 23 Clientes Rev 3 Industrial sanidad.pdf",
                mime="Doc/pdf",
                use_container_width=True
                )        
        with col16:
            st.image('https://i.imgur.com/6zK69Kq.jpg')

    def sp24():
        col11,col12 = st.columns(2)
        with col11:
            st.markdown("<h4 style='text-align: center;'>SP-24</h4>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Composición: 1 Celda de 5 Gr</p>", unsafe_allow_html=True)
            DSP520 = pd.DataFrame({
            'Caudal O2 (l/min)': [1],
            'Conc. O3 (gr/m3)': [42.8],
            'Prod. O3 (g/h)': [2.58]
            })
            st.dataframe(DSP520, hide_index=True, use_container_width=True)
            with open("Ficha tecnica SP 24 v3.pdf", "rb") as file:
                    btn5 = st.download_button(
                    label="Ficha Técnica",
                    data=file,
                    file_name="Ficha tecnica SP 24 v3.pdf",
                    mime="Doc/pdf",
                    use_container_width=True
                    )
        with col12:
            st.image('https://i.imgur.com/mcAZEg0.jpg')

    def sp25():
        col24,col25 = st.columns(2)
        with col24:
            st.markdown("<h4 style='text-align: center;'>SP-25 40 gr</h4>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Composición: 2 Celdas OC15 en serie</p>", unsafe_allow_html=True)
            DSP25 = pd.DataFrame({
            'Caudal O2 (l/min)': [1,2,3,4,5,6,7,8,9],
            'Conc. O3 (gr/m3)': [70,71,72,70,67,60,59,56,52],
            'Prod. O3 (g/h)': [4.2,8.52,12.96,16.8,20.1,21.6,24.78,26.88,28.08]
            })
            st.dataframe(DSP25, hide_index=True, use_container_width=True)
            with open("Ficha tecnica SP 25.pdf", "rb") as file:
                btn2 = st.download_button(
                label="Ficha Técnica",
                data=file,
                file_name="Ficha tecnica SP 25.pdf",
                mime="Doc/pdf",
                use_container_width=True
                )        
        with col25:
            st.image('https://i.imgur.com/OI3WF8q.jpg')


    if calcule == True:
        st.markdown("<h3 style='text-align: center;'>Sistemas Recomendados</h3>", unsafe_allow_html=True)
        if Pr>=0 and Pr<=2:
            sp24()

        if Pr>2 and Pr<=12:
            sp520()
            sp545()
            sp560()
            sp18()

        if Pr>12 and Pr<=20:
            sp520()
            sp545()
            sp560()
            sp18()
            sp2060()
            sp2080()
            sp23()
            sp25()

        if Pr>20:
            st.markdown("<h4 style='text-align: center;'>NOTA: Para concentraciones mayores a 28 gr/h considere la combinación de 2 o mas sistemas</h4>", unsafe_allow_html=True)
            sp545()
            sp560()
            sp18()
            sp2060()
            sp2080()
            sp23()
                
    st.divider()
    st.markdown("<h3 style='text-align: center;'>Curvas de desinfección del Agua: Concentración vs. Redox", unsafe_allow_html=True)
    st.image("https://i.imgur.com/cQ1fWXQ.jpg")


#OZONE IN AIR CALCULE
    
if option == "Ozono Aire":

    st.selectbox('Seleccione un equipo:',(
        'Z1250T - Prod. Nominal: 17 mg/h',
        'Z3000T - Prod. Nominal: 34 mg/h',
        'Z6000T - Prod. Nominal: 75 mg/h',
        'Z10000T - Prod. Nominal: 95 mg/h',
        'Z20000T - Prod. Nominal: 120 mg/h',
        'ZHI1250 - Prod. Nominal: 17 mg/h',
        'ZHI3000 - Prod. Nominal: 34 mg/h',
        'ZHI6000 - Prod. Nominal: 75 mg/h',
        'ZHI10000 - Prod. Nominal: 95 mg/h',
        'ZHI300MG - Prod. Nominal: 0.3 gr/h',
        'ZHI500MG - Prod. Nominal: 0.3 gr/h',
        'ZHI1000MG - Prod. Nominal: 0.55 gr/h',
        'SPMINI300MG - Prod. Nominal: 0.3 gr/h',
        'SPMINI500MG - Prod. Nominal: 0.35 gr/h',
        'SPMINI1G - Prod. Nominal: 0.42 gr/h',
        'SPMINI2G - Prod. Nominal: 3.2 gr/h',
        'SP300MG - Prod. Nominal: 0.3 gr/h',
        'SP500MG - Prod. Nominal: 0.35 gr/h',
        'SP1G - Prod. Nominal: 0.42 gr/h',
        'SP2G - Prod. Nominal: 3.2 gr/h',
        'SP4G - Prod. Nominal: 4 gr/h',
        'SP8G - Prod. Nominal: 4.62 gr/h',
        'SP10G - Prod. Nominal: 6.4 gr/h',
        'SP15G - Prod. Nominal: 4.5 gr/h'
    ), index=None)

    st.divider()
    col17,col18,col19 = st.columns(3)
    with col17:
        Ve = st.number_input("Volumen del espacio a tratar (L)", value=None)
    with col18:
        Qg = st.number_input("Caudal de salida del gas (L/min)", value=None)
    with col19:
        Pr = st.number_input("Producción seleccionada (g/h)", value=None)
    

    col1,col2,col3 = st.columns(3)
    with col1:
        st.markdown("<p style='text-align: center;'>Concentración (g/m3)</p>", unsafe_allow_html=True)
        if Pr == None:
            Co = 0
        else:
            Co=float("{:.2f}".format((Pr/(Qg*60))*1000))
        st.markdown("<p style='text-align: center;'>{}</p>".format(str(Co)), unsafe_allow_html=True)
    with col2:
        st.markdown("<p style='text-align: center;'>Constante K</p>", unsafe_allow_html=True)
        k = 1.65
        st.markdown("<p style='text-align: center;'>{}</p>".format(str(k)), unsafe_allow_html=True)
    with col3:
        fi = st.slider("Factor de Intercambio", min_value=0.5, max_value=1.2, value=0.8)
        
    calcule = st.button("Calcular",use_container_width=True)

    if calcule == True:
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

st.markdown("<p style='text-align: center; color:gray; font-size: 14px;'> © 2024 PID Medioambiental, S.L. <br> J. Aguilar <br> Rev. 1.01 </p>", unsafe_allow_html=True)