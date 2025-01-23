from pathlib import Path

import streamlit as st
import pandas as pd
from datetime import datetime

from utilidades import leitura_de_dados

leitura_de_dados()

df_insumos = st.session_state['dados']['df_insumos']
df_cad = st.session_state['dados']['df_cad']

local_insumo = df_cad['Linha'].tolist()

st.sidebar.markdown('## Adição de insumos')

local_selecionado = st.sidebar.selectbox('Selecione o local:',
                                            local_insumo)

Insumo = df_cad.loc[df_cad['Linha'] == local_selecionado, 'Insumo'].iloc[0]
Insumo = Insumo.strip('][').replace("'", '').split(', ')

Insumo_selecionado = st.sidebar.selectbox('Selecione o Insumo:',
                                            Insumo)

Insumo = "['Bending', 'Anticostela']"

qtd_insumos = st.sidebar.text_input('QTD')
novos_insumos = st.sidebar.text_input('Novos')
retifica_insumos = st.sidebar.text_input('Retífica')

Adicionar_dados = st.sidebar.button('Adicionar dados')
if Adicionar_dados:
    lista_adicionar = [df_insumos['id_de_lançamento'].max() + 1,
                        local_selecionado,
                        Insumo_selecionado,
                        novos_insumos,
                        retifica_insumos,
                        qtd_insumos]
    hora_adicionar = datetime.now()
    df_insumos.loc[hora_adicionar] = lista_adicionar
    caminho_datasets = st.session_state['caminho_datasets']
    df_insumos.to_csv(caminho_datasets / 'Insumos.csv', decimal=',', sep=';')
    st.success('Insumos para GAL 2 Adicionados com sucesso!')
   
    
st.sidebar.markdown('## Remoção de dados')
id_remocao = st.sidebar.number_input('ID na tabela a ser removido:',
                                     0,
                                     df_insumos['id_de_lançamento'].max())
remover_dados = st.sidebar.button('Remover Linha')
if remover_dados:
    df_insumos = df_insumos[df_insumos['id_de_lançamento'] != id_remocao]
    caminho_datasets = st.session_state['caminho_datasets']
    df_insumos.to_csv(caminho_datasets / 'Insumos.csv', decimal=',', sep=';')
    st.session_state['dados']['df_insumos'] = df_insumos


st.dataframe(df_insumos, height=800)