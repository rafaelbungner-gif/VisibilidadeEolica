import streamlit as st
import streamlit.components.v1 as components

# Configura a página para ocupar a tela toda
st.set_page_config(layout="wide", page_title="Dashboard Eólica")

# Lê o arquivo HTML que criamos
with open("visibilidade.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Renderiza o HTML dentro do Streamlit (ajuste a altura conforme necessário)
components.html(html_code, height=1200, scrolling=True)
