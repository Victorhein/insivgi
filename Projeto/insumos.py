from pathlib import Path

import pandas as pd 
import streamlit as st 

pasta_datasets = Path(__file__).parent.parent / 'datasets'
df_insumos = pd.read_csv(pasta_datasets / 'Insumos.csv', decimal=',', sep=';', index_col=0)

#                              >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

colunas = list(df_insumos.columns)
colunas_selecionadas = st.sidebar.multiselect('Selecione as colunas:', colunas, colunas)# Criando meu selecionador de colunas (Codigo presente na documentação do streamlit)

col1, col2 = st.sidebar.columns(2)
col_filtro = col1.selectbox('Selecione a coluna', colunas)
valor_filtro = col2.selectbox('Selecione o valor', list(df_insumos[col_filtro].dropna().unique()))
    
status_filtrar = col1.button('Filtrar')
status_limpar = col2.button('Limpar')

if status_filtrar:
    st.dataframe(df_insumos.loc[df_insumos[col_filtro] == valor_filtro, colunas_selecionadas], height=800)
elif status_limpar:
    st.dataframe(df_insumos[colunas_selecionadas], height=800)
else:
    st.dataframe(df_insumos[colunas_selecionadas], height=800)      