import pandas as pd
import streamlit as st
import altair as alt

# Chamada do set_page_config apenas uma vez, no início do script
st.set_page_config(page_title="Dashboard", layout="wide")

#paginas de interação
perfomance_page = st.navigation([st.Page("perfomance.py")])
# financeiro_page = st.navigation([st.Page("financeiro.py")])

# Navegação entre páginas usando condicional
pages = st.sidebar.selectbox("Escolha uma página", ["Home", "Perfomance"])
st.logo("https://i.imgur.com/78iKILX.png")

# Condições para navegar nas paginas
if pages == "Home":
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write("")
    with col2:
        st.write("")
    with col3:
        st.image("https://i.imgur.com/d9G5U0e.png")
    with col4:
        st.write("")
    with col5:
        st.write("")


elif pages == "Perfomance":
    # Adicione o código da página perfomance aqui diretamente
    # Ou importe como função e execute
    perfomance_page.run()

# elif pages == "Financeiro":
#     # financeiro_page.run()
