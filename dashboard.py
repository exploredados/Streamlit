import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar a base de dados
file_path = r"C:\Users\bruno.patricio\OneDrive - Unimedpoa\Área de Trabalho\power treinamento.xlsx"
df = pd.read_excel(file_path)

# Gráfico de colunas: a quantidade de Nome por Setor
nome_por_setor = df.groupby('Setor')['Nome'].count().reset_index()
fig_colunas = px.bar(nome_por_setor, x='Setor', y='Nome', title='Quantidade de Nomes por Setor')

# Gráfico de barras: a quantidade de Setor
quantidade_setor = df['Setor'].value_counts().reset_index()
quantidade_setor.columns = ['Setor', 'Quantidade']
fig_barras = px.bar(quantidade_setor, x='Setor', y='Quantidade', title='Quantidade de Setores')

# Card informativo com a quantidade de Nomes
quantidade_nomes = df['Nome'].nunique()

# Configurar o layout do dashboard no Streamlit
st.title('Dashboard de Treinamento')
st.header('Informações Gerais')

# Mostrar o card informativo
st.metric(label="Quantidade de Nomes", value=quantidade_nomes)

# Mostrar os gráficos
st.plotly_chart(fig_colunas)
st.plotly_chart(fig_barras)
