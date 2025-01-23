from pathlib import Path
import pandas as pd 

from datetime import datetime
import streamlit as st 

pasta_datasets = Path(__file__).parent.parent / 'datasets'
df_insumos = pd.read_csv(pasta_datasets / 'Insumos.csv', decimal=',', sep=';', index_col=0)
df_cad = pd.read_csv(pasta_datasets / 'cad.csv', decimal=',', sep=';', index_col=0)

lista_cad = df_cad['Linha'].to_list()
cad_selecionado = st.sidebar.selectbox('Selecione o local:', 
                                        lista_cad)

lista_insumos = df_cad.loc[df_cad['Linha'] == cad_selecionado, 'Insumo'].iloc[0]
lista_insumos = lista_insumos.strip('][').replace("'", '').split(', ')
insumo_selecionado = st.sidebar.selectbox('Selecione o insumo:',
                                            lista_insumos)

qtd_insumos = st.sidebar.text_input('QTD')
novos_insumos = st.sidebar.text_input('Novos')
retifica_insumos = st.sidebar.text_input('Retífica')

if st.sidebar.button('Adicionar dados'):
    lista_adicionar = [df_insumos['id_de_lançamento'].max() + 1,
                        insumo_selecionado,
                        cad_selecionado,
                        qtd_insumos,
                        novos_insumos,
                        retifica_insumos]
    df_insumos.loc[datetime.now()] = lista_adicionar
    df_insumos.to_csv(pasta_datasets / 'Insumos.csv', decimal=',', sep=';')
    st.success('Insumos para GAL 2 Adicionados com sucesso!')


st.dataframe(df_insumos, height=800)
