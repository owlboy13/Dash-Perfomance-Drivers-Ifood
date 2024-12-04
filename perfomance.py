import pandas as pd
import streamlit as st
import altair as alt
import datetime as dt
import numpy as np
import plotly.express as px
import openpyxl

# Otimização: Cache para o carregamento dos dados
@st.cache_data
def carregar_dados():
    return pd.read_excel('perfomance.xlsx', dtype={'pessoa_entregadora': 'str', 'data_do_periodo': 'str', 'numero_de_corridas_completadas': 'int'})

# Carregar planilha de forma eficiente
planilha = carregar_dados()

# Converter a coluna de data para datetime, ignorando horas e erros de conversão
planilha['data_do_periodo'] = pd.to_datetime(planilha['data_do_periodo'], errors='coerce').dt.date

# Definir datas de início e fim
end_date = dt.date.today()
start_date = dt.date(end_date.year, end_date.month, end_date.day)

# Dados do Streamlit
st.header("Perfomance - Drivers :chart_with_upwards_trend:")

# Selecionar período
with st.container():
    st.subheader('Selecione o período: ')
    col1, col2 = st.columns(2)

    with col1:
        data_inicial = st.date_input('Selecione a data inicial:', start_date)
    with col2:
        data_final = st.date_input('Selecione a data final:', end_date)

# Filtrar por período antes de selecionar os entregadores
filtered_period = planilha[(planilha['data_do_periodo'] >= data_inicial) &
                           (planilha['data_do_periodo'] <= data_final)]

# Obter apenas os nomes únicos dos entregadores no período filtrado
names_planilha = filtered_period['pessoa_entregadora'].unique()

# Selecionar entregador (sem repetição de nomes)
with st.container():
    box_driver = st.selectbox('Selecione o entregador:', options=names_planilha)
    st.write(f"Informações do entregador: {box_driver}")

# Filtrar dados com base no entregador e período selecionados
filtered_data = filtered_period[filtered_period['pessoa_entregadora'] == box_driver]

# Soma de rotas completas por entregador
with st.container():
    coluna1, coluna2, coluna3, coluna4, coluna5 = st.columns(5)
    rotas_completas = filtered_data['numero_de_corridas_completadas'].sum()
    rotas_aceitas = filtered_data['numero_de_corridas_aceitas'].sum()
    rejeitadas = filtered_data['numero_de_corridas_rejeitadas'].sum()
    ofertadas = filtered_data['numero_de_corridas_ofertadas'].sum()
    tempo_online = filtered_data['TEMPO'].mean()

    coluna1.metric("Rotas Completas", rotas_completas)
    coluna2.metric("Rotas Rejeitadas", rejeitadas)
    coluna3.metric("Ofertadas", ofertadas)
    coluna4.metric("Aceitas", rotas_aceitas)
    coluna5.metric("Tempo Online", tempo_online,'%')

# Verificar se há dados correspondentes
if not filtered_data.empty:
    # Criar DataFrame com as métricas
    grafico_horizontal = pd.DataFrame({
        'Métricas': ['TEMPO', 'ACEITAS', 'COMPLETAS'],
        'Percentual %': [filtered_data['TEMPO'].mean(), 
                         filtered_data['ACEITAS'].mean(), 
                         filtered_data['COMPLETAS'].mean()]
    })

    # Criar gráfico de barras horizontal usando Altair
    bar_chart = alt.Chart(grafico_horizontal).mark_bar().encode(
        x='Percentual %',
        y=alt.Y('Métricas', sort='-x'),
        color='Métricas',
        tooltip=['Métricas', 'Percentual %']
    ).properties(
        width=400,
        height=200,
    )

    # Exibir gráfico no Streamlit
    st.altair_chart(bar_chart, use_container_width=True)

    st.subheader("Gráficos de Rotas:", divider=True)

    with st.container():

        min_chart1, min_chart2, min_chart3 = st.columns(3)
        
        with min_chart1:
            # Criar o DataFrame para o gráfico de linhas, agora com dados reais de rotas completas por data
            chart_data = filtered_data[['data_do_periodo', 'numero_de_corridas_completadas']].copy()
            chart_data = chart_data.rename(columns={'data_do_periodo': 'Período', 'numero_de_corridas_completadas': 'Nº Rotas Completas'})

            # Criar gráfico de dispersão interativo usando Plotly
            fig = px.scatter(chart_data, x='Período', y='Nº Rotas Completas', title="Completas")

            # Exibir gráfico com Plotly no Streamlit e ativar a interatividade com 'on_select'
            event = st.plotly_chart(fig, key="rotas_completas", on_select="rerun")


        with min_chart2:
            chart_data2 = filtered_data[['data_do_periodo', 'numero_de_corridas_rejeitadas']].copy()
            chart_data2 = chart_data2.rename(columns={'data_do_periodo': 'Período', 'numero_de_corridas_rejeitadas': 'Nº Rotas Rejeitadas'})

            # Criar gráfico de dispersão interativo usando Plotly
            fig2 = px.scatter(chart_data2, x='Período', y='Nº Rotas Rejeitadas', title="Rejeitadas")

            # Exibir gráfico com Plotly no Streamlit e ativar a interatividade com 'on_select'
            event2 = st.plotly_chart(fig2, key="rejeitadas", on_select="rerun")
        with min_chart3:
            chart_data3 = filtered_data[['data_do_periodo', 'numero_de_corridas_ofertadas']].copy()
            chart_data3 = chart_data3.rename(columns={'data_do_periodo': 'Período', 'numero_de_corridas_ofertadas': 'Nº Rotas OFertadas'})

            # Criar gráfico de dispersão interativo usando Plotly
            fig3 = px.scatter(chart_data3, x='Período', y='Nº Rotas OFertadas', title="Ofertadas")

            # Exibir gráfico com Plotly no Streamlit e ativar a interatividade com 'on_select'
            event3 = st.plotly_chart(fig3, key="ofertadas", on_select="rerun")
            
else:
    st.write("Nenhum dado encontrado para o entregador ou período selecionado.")
