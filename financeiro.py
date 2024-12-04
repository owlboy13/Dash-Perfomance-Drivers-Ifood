import pandas as pd
import streamlit as st
import altair as alt
import datetime as dt
import numpy as np
import plotly.express as px

# Otimização: Cache para o carregamento dos dados
@st.cache_data
def dados_financeiro():
    return pd.read_excel('financeiro.xlsx', dtype={'recebedor': 'str', 'data_do_periodo_de_referencia': 'str', 'valor': 'float'})

# Carregar planilha de forma eficiente
planilha = dados_financeiro()
with st.container():
    st.dataframe(planilha.head(15),1000,500)
