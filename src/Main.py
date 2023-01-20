import streamlit as st
import pandas as pd
import numpy as np


################################## Configurações de página ####################################
st.set_page_config(
    page_title="Processo seletivo Legisla",
    layout="wide",
)
################################## Funções de dados ############################################
@st.cache
def get_dados():
    df = pd.read_csv('./src/data/Analista de Dados e BI - Pedro Campos _ Case técnico - Página1.csv',sep=',')
    df = limpa_dados(df)
    return df
@st.cache
def get_estados():
    return get_dados()['Estado '].unique()

def limpa_dados(df):
    df['Ano de ingresso no Congresso'] = df['Ano de ingresso no Congresso'].str.replace('[^\d]','',regex=True)
    df['Ano de ingresso no Congresso'] = df['Ano de ingresso no Congresso'].astype('int')
    df['Idade que começou a trabalhar'] = df['Idade que começou a trabalhar'].str.replace('[^\d]','',regex=True)
    df['Idade que começou a trabalhar'] = df['Idade que começou a trabalhar'].astype('int')
    df['Cor'] = np.where(df['Cor'] == 'Pessoa Branca','Branca',
                    np.where(df['Cor'] == 'Pessoa Preta','Preta',
                        np.where(df['Cor'] == 'Pessoa Amarela','Amarela',
                            np.where(df['Cor'] == 'Pardo','Parda',df['Cor'])
                        )
                    )
                )
    df['Orçamento disponível '] = df['Orçamento disponível '].str.replace('[R\$ \.]','',regex=True).str.replace(',','.').astype('float')
    return df
################################## Header ######################################################
st.markdown("""# Painel para a identificação de perfil e orçamento gerido""")
st.write("---")
################################## Filtros #####################################################
filtro = st.expander(':mag:Filtros')
col1, col2 = filtro.columns(2)
selecao_estado = col1.selectbox(label='Estado',options= get_estados(),)
