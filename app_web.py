import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Mi Mini Empresa", page_icon="📦", layout="centered")

st.title("📦 Sistema de Productos - Mi Mini Empresa")

archivo = "productos.csv"

# Si no existe el archivo, crearlo vacío
if not os.path.exists(archivo):
    df = pd.DataFrame(columns=["id", "name", "qty", "price", "desc"])
    df.to_csv(archivo, index=False)

# Leer datos
df = pd.read_csv(archivo)

st.subheader("Agregar nuevo producto")
with st.form("form_producto"):
    nombre = st.text_input("Nombre del producto")
    cantidad = st.number_input("Cantidad", min_value=0, step=1)
    precio = st.number_input("Precio (S/.)", min_value=0.0, step=0.1)
    descripcion = st.text_area("Descripción")
    submit = st.form_submit_button("Guardar")

    if submit:
        nuevo = pd.DataFrame({
            "id": [len(df) + 1],
            "name": [nombre],
            "qty": [cantidad],
            "price": [precio],
            "desc": [descripcion]
        })
        df = pd.concat([df, nuevo], ignore_index=True)
        df.to_csv(archivo, index=False)
        st.success("✅ Producto guardado correctamente.")

st.subheader("📋 Lista de productos")
st.dataframe(df)
