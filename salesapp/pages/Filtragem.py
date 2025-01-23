from pathlib import Path

import streamlit as st
import pandas as pd

if not 'dados' in st.session_state: # criar uma session para manter os dados entre as paginas 
    pasta_datasets = Path(__file__).parent.parent.parent / 'datasets'
    df_insumos = pd.read_csv(pasta_datasets / 'Insumos.csv', decimal=',', sep=';', index_col=0, parse_dates=True)
    df_cad = pd.read_csv(pasta_datasets / 'cad.csv', decimal=',', sep=';', index_col=0)
    dados = {'df_insumos': df_insumos,
             'df_cad': df_cad}
    st.session_state['dados'] = dados

df_insumos = st.session_state['dados']['df_insumos']
df_cad = st.session_state['dados']['df_cad']



def mostra_tabela_cad():
    st.dataframe(df_cad)
    
def mostra_tabela_insumos():
    st.sidebar.divider()
    st.sidebar.markdown('## Filtrar tabela')
    Colunas_selecionadas = st.sidebar.multiselect('Selecione as colunas da tabela:',
                                                  list(df_insumos.columns),
                                                  list(df_insumos.columns))
    
    col1, col2 = st.sidebar.columns(2)
    filtro_selecionado = col1.selectbox('Filtrar coluna', list(df_insumos.columns))
    
    valores_unicos_coluna = list(df_insumos[filtro_selecionado].unique())
    valor_filtro = col2.selectbox('Valor do filtro', valores_unicos_coluna)

    filtrar = col1.button('Filtrar')
    limpar = col2.button('Limpar')

    if filtrar:
         st.dataframe(df_insumos.loc[df_insumos[filtro_selecionado] == valor_filtro, Colunas_selecionadas], height=800)
    elif limpar:
        st.dataframe(df_insumos[Colunas_selecionadas], height=800)
    else:
        st.dataframe(df_insumos[Colunas_selecionadas], height=800)

    
    
    

st.sidebar.markdown('# Seleção de tabelas')
tabela_selecionada = st.sidebar.selectbox('Selecione a tabela que você deseja ver:',
                     ['Controle', 'Itens'])




if tabela_selecionada == 'Controle':
    mostra_tabela_insumos()
elif tabela_selecionada == 'Itens':
    mostra_tabela_cad()











