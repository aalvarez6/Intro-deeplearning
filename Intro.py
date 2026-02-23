import streamlit as st

st.title("Mi primera APP interactiva")
#st.subtitle 
#Texto
st.write ("Determinar que tan bien estoy haciendo los estiramientos de YOGA")
#Entrada de texto
nombre = st.text_input ("Escribe tu nombre:")
# Boton
if st.button ("Saludar"):
  st.success(f"hola {nombre}, bienvenido a YoGiOH!)

# Slider
edad = st.slider("seleciona tu edad", 0, 100, 25)
st.write("Tu edad es:", edad)

