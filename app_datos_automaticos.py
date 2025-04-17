# Importamos las herramientas mágicas (como varitas para construir nuestro castillo)
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import base64
from io import BytesIO
import os
from PIL import Image

# Configuramos la página para que se vea grande y bonita
st.set_page_config(
    page_title="Tablero Ejecutivo Lazzar",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Función para cargar el archivo Excel (como abrir un libro de cuentos)
@st.cache_data
def load_data(file_path):
    try:
        df = pd.read_excel(file_path)
        # Cambiamos los nombres de las columnas para que sean más claros
        expected_columns = {
            'Agente': 'Agente',
            'ACUMULADO CHATS': 'Chats Atendidos',
            'ACUMULADO VENTAS CERRADAS': 'Ventas Convertidas'
        }
        df = df.rename(columns=expected_columns)
        # Limpiamos los datos para que no haya números raros
        df['Chats Atendidos'] = pd.to_numeric(df['Chats Atendidos'], errors='coerce').fillna(0).astype(int)
        df['Ventas Convertidas'] = pd.to_numeric(df['Ventas Convertidas'], errors='coerce').fillna(0).astype(int)
        return df
    except Exception as e:
        st.error(f"Error al cargar el archivo: {e}")
        return None

# Función para hacer que el castillo brille con colores mágicos
def apply_custom_css():
    st.markdown("""
    <style>
    /* Fondo del castillo con un cielo estrellado */
    .stApp {
        background: linear-gradient(135deg, #0d1b2a 0%, #1b263b 100%);
        color: #f5f5f5;
        font-family: 'Orbitron', sans-serif;
    }
    /* Títulos que brillan como estrellas doradas */
    h1, h2, h3 {
        font-family: 'Cinzel', serif;
        color: #ffd700;
        text-shadow: 0 0 10px #ffd700, 0 0 20px #ffd700;
        animation: glow 2s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from { text-shadow: 0 0 10px #ffd700, 0 0 20px #ffd700; }
        to { text-shadow: 0 0 20px #ffd700, 0 0 30px #ffaa00; }
    }
    /* Botones que parecen joyas */
    .stButton>button {
        background: linear-gradient(45deg, #ffd700, #ffaa00);
        color: #0d1b2a;
        border-radius: 15px;
        font-weight: bold;
        font-family: 'Orbitron', sans-serif;
        transition: all 0.5s ease;
        border: none;
        box-shadow: 0 0 15px #ffd700;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #ffaa00, #ffd700);
        transform: scale(1.1);
        box-shadow: 0 0 25px #ffaa00;
    }
    /* Tarjetas de datos que flotan como naves espaciales */
    .metric-card {
        background: rgba(27, 38, 59, 0.9);
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #ffd700;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
        transition: all 0.5s ease;
        animation: float 3s ease-in-out infinite;
    }
    .metric-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.8);
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    /* Tablas que parecen pantallas futuristas */
    .dataframe {
        border: 2px solid #ffd700;
        border-radius: 10px;
        background-color: rgba(27, 38, 59, 0.8);
        color: #f5f5f5;
    }
    /* Barra lateral como un panel de control de nave espacial */
    .css-1d391kg {
        background: linear-gradient(180deg, #0d1b2a 0%, #1b263b 100%);
        border-right: 3px solid #ffd700;
    }
    </style>
    """, unsafe_allow_html=True)

# Función para cargar el logo (como poner una bandera en el castillo)
def get_base64_image(image_path):
    try:
        img = Image.open(image_path)
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()
    except:
        return None

# Hacemos que el castillo brille con nuestro diseño mágico
apply_custom_css()

# Barra lateral (como un panel de control para elegir cosas)
st.sidebar.markdown("""
    <div style='text-align: center;'>
        <h2>Panel de Control Lazzar</h2>
    </div>
""", unsafe_allow_html=True)

# Intentamos cargar el logo (como poner una bandera bonita)
logo_path = "logo_lazzar.png"
if os.path.exists(logo_path):
    logo_base64 = get_base64_image(logo_path)
    st.sidebar.markdown(
        f'<img src="data:image/png;base64,{logo_base64}" width="150" style="margin-bottom:20px;">',
        unsafe_allow_html=True
    )
else:
    st.sidebar.image("https://via.placeholder.com/150", caption="Logo Lazzar")

# Agregamos una contraseña para que solo el creador pueda subir el archivo
st.sidebar.subheader("Acceso para el Creador")
password = st.sidebar.text_input("Ingresa la contraseña", type="password")
correct_password = "lazzar2025"  # Esta es la contraseña secreta (puedes cambiarla)

# Solo mostramos el botón de subir archivo si la contraseña es correcta
if password == correct_password:
    st.sidebar.success("¡Contraseña correcta! Puedes subir el archivo.")
    uploaded_file = st.sidebar.file_uploader("Sube tu archivo Excel", type=["xlsx"])
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        df = df.rename(columns={
            'Agente': 'Agente',
            'ACUMULADO CHATS': 'Chats Atendidos',
            'ACUMULADO VENTAS CERRADAS': 'Ventas Convertidas'
        })
        df['Chats Atendidos'] = pd.to_numeric(df['Chats Atendidos'], errors='coerce').fillna(0).astype(int)
        df['Ventas Convertidas'] = pd.to_numeric(df['Ventas Convertidas'], errors='coerce').fillna(0).astype(int)
    else:
        file_path = "ACUMULADO VENTAS DE CHATS MARZO CORRECIÓN 2025.xlsx"
        df = load_data(file_path)
else:
    # Si la contraseña no es correcta, cargamos el archivo predeterminado
    if password != "":
        st.sidebar.error("Contraseña incorrecta. Solo el creador puede subir un nuevo archivo.")
    file_path = "ACUMULADO VENTAS DE CHATS MARZO CORRECIÓN 2025.xlsx"
    df = load_data(file_path)

# Verificamos que el libro de datos se haya abierto bien
if df is not None:
    # Filtros en el panel de control
    st.sidebar.subheader("Filtros Mágicos")
    agentes = st.sidebar.multiselect("Elige Agentes", options=df['Agente'].unique(), default=df['Agente'].unique())
    min_chats, max_chats = st.sidebar.slider(
        "Rango de Chats Atendidos",
        int(df['Chats Atendidos'].min()), int(df['Chats Atendidos'].max()),
        (int(df['Chats Atendidos'].min()), int(df['Chats Atendidos'].max()))
    )

    # Filtramos los datos según lo que eligieron
    filtered_df = df[
        (df['Agente'].isin(agentes)) &
        (df['Chats Atendidos'].between(min_chats, max_chats))
    ]

    # Título principal (como un letrero gigante en el castillo)
    st.markdown("<h1 style='text-align: center;'>Tablero Ejecutivo Lazzar</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Análisis de Ventas y Chats - Marzo 2025</h3>", unsafe_allow_html=True)

    # Tarjetas con números importantes (como pantallas brillantes)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            f"<div class='metric-card'><h3>Total Agentes</h3><p style='font-size:24px;'>{len(filtered_df['Agente'].unique())}</p></div>",
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            f"<div class='metric-card'><h3>Chats Atendidos</h3><p style='font-size:24px;'>{filtered_df['Chats Atendidos'].sum():,}</p></div>",
            unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            f"<div class='metric-card'><h3>Ventas Convertidas</h3><p style='font-size:24px;'>{filtered_df['Ventas Convertidas'].sum():,}</p></div>",
            unsafe_allow_html=True
        )

    # Gráfico de barras (como torres de colores para cada agente)
    st.subheader("Ventas Convertidas por Agente")
    # Ordenamos los datos de mayor a menor según Ventas Convertidas
    filtered_df_sorted = filtered_df.sort_values(by='Ventas Convertidas', ascending=False)
    fig_bar = px.bar(
        filtered_df_sorted,
        x='Agente',
        y='Ventas Convertidas',
        color='Agente',
        title="Desempeño de Ventas por Agente",
        height=600,
        template='plotly_dark'
    )
    fig_bar.update_layout(
        font_family="Orbitron",
        font_size=14,
        title_font_family="Cinzel",
        title_font_size=24,
        xaxis_title="Agente",
        yaxis_title="Ventas Convertidas",
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    # Gráfico de dispersión (como estrellitas que muestran chats y ventas)
    st.subheader("Relación entre Chats Atendidos y Ventas Convertidas")
    # Usamos los datos ordenados
    fig_scatter = px.scatter(
        filtered_df_sorted,
        x='Chats Atendidos',
        y='Ventas Convertidas',
        color='Agente',
        size='Ventas Convertidas',
        hover_data=['Agente'],
        title="Eficiencia de Conversión por Agente",
        height=600,
        template='plotly_dark'
    )
    fig_scatter.update_layout(
        font_family="Orbitron",
        font_size=14,
        title_font_family="Cinzel",
        title_font_size=24,
        xaxis_title="Chats Atendidos",
        yaxis_title="Ventas Convertidas",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        # Hacemos la leyenda más grande y clara
        legend=dict(
            title="Agentes",
            font=dict(size=16, family="Orbitron", color="#ffd700"),
            bgcolor='rgba(0,0,0,0)',
            bordercolor="#ffd700",
            borderwidth=1,
            itemsizing='constant'
        ),
        scattermode='group'
    )
    # Hacemos que los puntitos tengan un tamaño mínimo para que sean más visibles
    fig_scatter.update_traces(marker=dict(sizemin=10))
    st.plotly_chart(fig_scatter, use_container_width=True)

    # Tabla con los datos (como una pantalla con información)
    st.subheader("Datos Detallados")
    st.dataframe(
        filtered_df_sorted[['Agente', 'Chats Atendidos', 'Ventas Convertidas']],
        use_container_width=True
    )

    # Botón para descargar los datos (como guardar un dibujo)
    def to_excel(df):
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Reporte')
        return output.getvalue()

    excel_data = to_excel(filtered_df_sorted)
    st.download_button(
        label="Descargar Reporte en Excel",
        data=excel_data,
        file_name="Reporte_Lazzar_Marzo_2025.xlsx",
        mime="application/vnd.ms-excel"
    )

else:
    st.error("Por favor, verifica que el archivo exista en la carpeta.")

# Pie de página (como una placa en el castillo)
st.markdown("""
    <hr style='border: 2px solid #ffd700;'>
    <p style='text-align: center; color: #ffd700; font-family: Orbitron;'>
        © 2025 Lazzar México - Desarrollado para la Dirección Comercial
    </p>
""", unsafe_allow_html=True)