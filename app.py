import streamlit as st
st.title("Ejemplo para usar sesión_ state")
count = 0

increment = st.button("increment")
if increment:
  count +=1
st.write("Count =, count")
