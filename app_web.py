import streamlit as st
import pandas as pd
from PIL import Image

# ----------------------------------------
# Configuración de la página
# ----------------------------------------
st.set_page_config(
    page_title="Mi App Empresa",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------
# Sidebar interactivo
# ----------------------------------------
st.sidebar.image("empresa_logo.png", width=150)  # logo de la empresa
st.sidebar.title("Menú de Navegación")
opcion = st.sidebar.radio(
    "Selecciona una sección",
    ["Inicio", "Productos", "Agregar Producto", "Estadísticas", "Contacto"]
)

st.sidebar.markdown("---")
st.sidebar.write("© 2025 Mi App Empresa")

# ----------------------------------------
# Sección: Inicio
# ----------------------------------------
if opcion == "Inicio":
    st.title("🌟 Bienvenido a Mi App Empresa")
    st.markdown(
        "Esta es una aplicación interactiva donde puedes ver productos, "
        "agregarlos, y revisar estadísticas de la empresa."
    )
    st.image(
        "https://cdn-icons-png.flaticon.com/512/2991/2991148.png",
        width=400
    )

# ----------------------------------------
# Sección: Productos
# ----------------------------------------
elif opcion == "Productos":
    st.header("📦 Lista de Productos")
    try:
        df_productos = pd.read_csv("productos.csv")
        st.dataframe(df_productos)
        st.markdown("### Filtrar productos")
        nombre_filtro = st.text_input("Buscar por nombre")
        if nombre_filtro:
            df_filtrado = df_productos[df_productos["nombre"].str.contains(nombre_filtro, case=False)]
            st.dataframe(df_filtrado)
    except FileNotFoundError:
        st.warning("No se encontró productos.csv")

# ----------------------------------------
# Sección: Agregar Producto
# ----------------------------------------
elif opcion == "Agregar Producto":
    st.header("➕ Agregar Nuevo Producto")
    with st.form(key="form_producto"):
        nombre = st.text_input("Nombre del producto")
        precio = st.number_input("Precio", 0.0, 10000.0)
        descripcion = st.text_area("Descripción")
        submit_button = st.form_submit_button(label="Guardar Producto")

    if submit_button:
        st.success(f"Producto **{nombre}** agregado con precio **S/.{precio}**")
        # Aquí podrías agregar lógica para guardar en CSV o DB

# ----------------------------------------
# Sección: Estadísticas
# ----------------------------------------
elif opcion == "Estadísticas":
    st.header("📊 Estadísticas de Ventas")
    data = {"Mes": ["Ene", "Feb", "Mar", "Abr"], "Ventas": [150, 200, 170, 300]}
    df = pd.DataFrame(data)
    st.bar_chart(df.set_index("Mes"))

    st.markdown("### KPI")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Ventas", "820", "+15%")
    col2.metric("Clientes Nuevos", "45", "+5%")
    col3.metric("Productos", "12", "0%")

# ----------------------------------------
# Sección: Contacto
# ----------------------------------------
elif opcion == "Contacto":
    st.header("📞 Contacto")
    st.write("Correo: contacto@miempresa.com")
    st.write("Teléfono: +51 999999999")
    col1, col2, col3 = st.columns(3)
    col1.image("https://cdn-icons-png.flaticon.com/512/733/733547.png", width=50)
    col2.image("https://cdn-icons-png.flaticon.com/512/733/733585.png", width=50)
    col3.image("https://cdn-icons-png.flaticon.com/512/732/732200.png", width=50)

# ----------------------------------------
# Footer
# ----------------------------------------
st.markdown("---")
st.markdown(
    "<center>© 2025 Mi App Empresa. Desarrollado por Raul Pazo</center>",
    unsafe_allow_html=True
)
