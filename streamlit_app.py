import streamlit as st

# Título de la aplicación
st.title("Formulario de Novedades")

# Campos del formulario
fecha = st.date_input("Fecha")
nombre = st.text_input("Nombre")
novedad = st.selectbox("Novedad", ["Llegada Tarde", "Incapacidad"])
detalles = st.text_area("Detalles")

# Botón para enviar los datos (en este caso, simplemente imprimimos los datos)
if st.button("Enviar"):
    st.write("Datos ingresados:")
    st.write(f"Fecha: {fecha}")
    st.write(f"Nombre: {nombre}")
    st.write(f"Novedad: {novedad}")
    st.write(f"Detalles: {detalles}")
