import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración del Título y la Descripción del Tablero
st.set_page_config(
    page_title="SMART KPI: Infraestructura de Datos y Cumplimiento Normativo (IDCN)",
    layout="wide"
)

# Título y Subtítulo
st.title("SMART KPI")
st.subheader("Infraestructura de Datos y Cumplimiento Normativo (IDCN)")

# Descripción general del tablero
st.markdown("""
Bienvenido al Tablero de Control para monitorear los indicadores clave relacionados con la 
**Infraestructura de Datos y Cumplimiento Normativo (IDCN)**. Este tablero incluye métricas clave para:
- **Tiempo de Consulta de Datos**: Velocidad y eficiencia en la consulta de información.
- **Porcentaje de Cumplimiento Normativo**: Grado de conformidad con regulaciones aplicables.
- **Eficiencia del Cumplimiento Estratégico**: Equilibrio entre cumplimiento normativo y aprovechamiento estratégico de los datos.
""")

# Simulación de datos para las métricas
data = {
    "Indicador": [
        "Velocidad de Respuesta (s)", 
        "Disponibilidad de Infraestructura (%)",
        "Auditorías Superadas sin Observaciones (%)",
        "Tiempo de Respuesta a Reguladores (días)",
        "Proporción de Datos Etiquetados (%)",
        "Índice de Integridad de Datos (%)"
    ],
    "Valor Actual": [1.8, 99.9, 95, 4.2, 92, 88],
    "Meta Objetivo": [2, 99.5, 100, 5, 90, 85]
}
df = pd.DataFrame(data)

# Sección de Resumen General
st.header("📈 Resumen General de Indicadores")
st.markdown("""
Esta sección proporciona una visión general de los principales indicadores del IDCN, comparando los valores actuales 
con los objetivos establecidos. Use los gráficos interactivos para profundizar en cada métrica.
""")

# Tabla Resumen
st.subheader("Tabla de Indicadores")
st.dataframe(df, use_container_width=True)

# Gráfico de Barras Comparativo
st.subheader("📊 Comparación de Valores Actuales vs. Metas")
fig_barras = px.bar(
    df, 
    x="Indicador", 
    y=["Valor Actual", "Meta Objetivo"], 
    barmode="group",
    labels={"value": "Valor", "Indicador": "Indicador Clave"},
    title="Comparación de Indicadores Clave"
)
st.plotly_chart(fig_barras, use_container_width=True)

# Sección Detallada: Tiempo de Consulta de Datos
st.header("⏱️ Tiempo de Consulta de Datos")
st.markdown("""
Monitoree la eficiencia de las consultas en la infraestructura de datos:
- **Velocidad de Respuesta**: Tiempo promedio de consulta.
- **Disponibilidad de Infraestructura**: Tiempo total operativo durante el período medido.
""")

fig_tiempo = px.line(
    x=["Enero", "Febrero", "Marzo", "Abril"],
    y=[2.0, 1.9, 1.7, 1.8],
    markers=True,
    labels={"x": "Mes", "y": "Velocidad de Respuesta (s)"},
    title="Velocidad Promedio de Respuesta Mensual"
)
st.plotly_chart(fig_tiempo, use_container_width=True)

# Sección Detallada: Cumplimiento Normativo
st.header("✅ Cumplimiento Normativo")
st.markdown("""
Explore el estado de conformidad con regulaciones clave:
- **Auditorías Superadas sin Observaciones**
- **Tiempo de Respuesta a Solicitudes Regulatorias**
- **Proporción de Datos Etiquetados con Metadatos de Conformidad**
""")

fig_cumplimiento = px.pie(
    values=[95, 5],
    names=["Cumplimiento", "Incumplimientos"],
    title="Distribución de Auditorías Superadas"
)
st.plotly_chart(fig_cumplimiento, use_container_width=True)

# Sección Estratégica: Eficiencia del Cumplimiento Estratégico
st.header("🔄 Eficiencia del Cumplimiento Estratégico")
st.markdown("""
Este índice mide el equilibrio entre cumplimiento normativo y aprovechamiento estratégico de datos.
""")

data_estrategico = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "Índice de Eficiencia (%)": [85, 87, 88, 90]
}
df_estrategico = pd.DataFrame(data_estrategico)

fig_estrategico = px.area(
    df_estrategico, 
    x="Mes", 
    y="Índice de Eficiencia (%)", 
    title="Tendencia del Índice de Eficiencia del Cumplimiento Estratégico"
)
st.plotly_chart(fig_estrategico, use_container_width=True)

# Conclusión
st.markdown("""
---
💡 **Nota:** Este tablero está diseñado para proporcionar información accionable y apoyar la toma de decisiones en tiempo real. 
Revisar periódicamente los valores de los indicadores garantiza una mejora continua en la gestión del IDCN.
""")
