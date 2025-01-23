from pathlib import Path

import streamlit as st
import pandas as pd

def leitura_de_dados():
    if not 'dados' in st.session_state: # criar uma session para manter os dados entre as paginas 
        pasta_datasets = Path(__file__).parents[1] / 'datasets'
        df_insumos = pd.read_csv(pasta_datasets / 'Insumos.csv', decimal=',', sep=';', index_col=0, parse_dates=True)
        df_cad = pd.read_csv(pasta_datasets / 'cad.csv', decimal=',', sep=';', index_col=0)
        dados = {'df_insumos': df_insumos,
                    'df_cad': df_cad}
        st.session_state['caminho_datasets'] = pasta_datasets
        st.session_state['dados'] = dados