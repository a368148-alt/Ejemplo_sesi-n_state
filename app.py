
import streamlit as st
st.title("Ejemplo para usar session_state")

if "count" not in st.session_state :
  st.session_state["count"] = 0

if "name" not in st.session_state:
  st.session_state["name"] = ""

if st.button("Click me"):
  st.session_state["count"] += 1

# Guardamos el valor del text_input directamente en session_state usando la clave "name"
st.text_input("Escribe tu nombre", key="name")

# Mostramos el nombre entre comillas
st.write(f'"{st.session_state["name"]}"')

st.write(st.session_state)
