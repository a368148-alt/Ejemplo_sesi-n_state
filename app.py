import streamlit as st
st.title("Ejemplo para usar sesion_ state")

if "count" not in st.sesion_state :
  st.sesion_state["count"] = 0

st.write(st.sesion_state)


