import streamlit as st
st.title("Ejemplo para usar sesión_ state")

if "count" not in st.sesión_state:
  st.sesión_state["count"] = 0

st.write(st.sesión_state)


