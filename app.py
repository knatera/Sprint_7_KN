#importar librerias
import pandas as pd
import plotly.express as px
import streamlit as st

#leer archivo de datos
car_data = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.header("Análisis de Datos con Streamlit y Plotly")

# crear un botón
hist_button = st.button('Construir histograma') 

# al hacer clic en el botón
if hist_button: 
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Botón para generar el gráfico de dispersión
if st.button("Generar Gráfico de Dispersión"):
    fig_scatter = px.scatter(car_data, x="columna_x", y="columna_y", title="Relación entre X e Y")
    st.plotly_chart(fig_scatter)