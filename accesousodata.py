import streamlit as st
import pandas as pd
import altair as alt

# Datos generados para el tablero de BI
data_sensing = pd.DataFrame({
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    'Precisión Predictiva (%)': [70, 75, 80, 78, 82, 85],
    'Tiempo de Detección (días)': [5, 4.8, 4.5, 4.7, 4.3, 4.0]
})

data_seizing = pd.DataFrame({
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    'Clientes Personalizados (%)': [20, 25, 30, 35, 40, 50],
    'Tasa de Conversión (%)': [10, 12, 15, 17, 20, 25]
})

data_configuring = pd.DataFrame({
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    'Tiempo de Consulta (segundos)': [30, 28, 25, 23, 20, 18],
    'Cumplimiento Normativo (%)': [90, 92, 93, 95, 96, 98]
})

# Descripción de las capacidades, metas, OKRs y KPIs
descriptions = {
    "Sensing": "Mejorar la calidad del monitoreo de datos para anticipar tendencias.",
    "Seizing": "Incrementar la personalización de productos para clientes.",
    "Configuring": "Optimizar la infraestructura de datos y garantizar el cumplimiento normativo."
}

okr_kpi_info = {
    "Sensing": {
        "OKR": "Lograr un monitoreo proactivo de datos de clientes para prever tendencias emergentes.",
        "KPI": "Precisión predictiva y tiempo promedio de detección."
    },
    "Seizing": {
        "OKR": "Ofrecer soluciones personalizadas a un 50% de la base de clientes existentes en seis meses.",
        "KPI": "Porcentaje de clientes personalizados y tasa de conversión."
    },
    "Configuring": {
        "OKR": "Establecer un lago de datos escalable y mejorar tiempos de consulta en un 40%.",
        "KPI": "Tiempo de consulta de datos y porcentaje de cumplimiento normativo."
    }
}

# Streamlit app
st.title("Tablero de Inteligencia Empresarial")
st.sidebar.title("Navegación")
option = st.sidebar.selectbox("Selecciona una capacidad", ["Sensing", "Seizing", "Configuring"])

# Mostrar descripciones y datos según la capacidad seleccionada
st.header(f"Capacidad: {option}")
st.subheader("Descripción")
st.write(descriptions[option])

st.subheader("Meta, OKR y KPI")
st.write(f"**OKR:** {okr_kpi_info[option]['OKR']}")
st.write(f"**KPI:** {okr_kpi_info[option]['KPI']}")

# Gráficos para cada capacidad
if option == "Sensing":
    st.subheader("Precisión Predictiva (%)")
    chart = alt.Chart(data_sensing).mark_line().encode(
        x='Mes',
        y='Precisión Predictiva (%)',
        tooltip=['Mes', 'Precisión Predictiva (%)']
    )
    st.altair_chart(chart, use_container_width=True)

    st.subheader("Tiempo de Detección (días)")
    chart = alt.Chart(data_sensing).mark_bar().encode(
        x='Mes',
        y='Tiempo de Detección (días)',
        tooltip=['Mes', 'Tiempo de Detección (días)']
    )
    st.altair_chart(chart, use_container_width=True)

elif option == "Seizing":
    st.subheader("Clientes Personalizados (%)")
    chart = alt.Chart(data_seizing).mark_line().encode(
        x='Mes',
        y='Clientes Personalizados (%)',
        tooltip=['Mes', 'Clientes Personalizados (%)']
    )
    st.altair_chart(chart, use_container_width=True)

    st.subheader("Tasa de Conversión (%)")
    chart = alt.Chart(data_seizing).mark_bar().encode(
        x='Mes',
        y='Tasa de Conversión (%)',
        tooltip=['Mes', 'Tasa de Conversión (%)']
    )
    st.altair_chart(chart, use_container_width=True)

elif option == "Configuring":
    st.subheader("Tiempo de Consulta (segundos)")
    chart = alt.Chart(data_configuring).mark_line().encode(
        x='Mes',
        y='Tiempo de Consulta (segundos)',
        tooltip=['Mes', 'Tiempo de Consulta (segundos)']
    )
    st.altair_chart(chart, use_container_width=True)

    st.subheader("Cumplimiento Normativo (%)")
    chart = alt.Chart(data_configuring).mark_bar().encode(
        x='Mes',
        y='Cumplimiento Normativo (%)',
        tooltip=['Mes', 'Cumplimiento Normativo (%)']
    )
    st.altair_chart(chart, use_container_width=True)

st.sidebar.info("Selecciona una capacidad para ver sus gráficos y métricas.")
