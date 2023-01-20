import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px

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

def get_dados_agrupados(df,dimensao,dimensao2=None):
    df_grp = df.groupby([dimensao]).count().rename(columns = {'Nome do Assessor' : 'Quantidade'}).reset_index()[[dimensao,'Quantidade']]
    if dimensao2!=None:
        df_parcial = df.groupby([dimensao,dimensao2]).count().rename( columns = {'Nome do Assessor' : 'Quantidade absoluta'}).reset_index()
        df_grp = df_grp.merge(df_parcial,how='inner',on=[dimensao])
        df_grp['Quantidade percentual'] = 100*df_grp['Quantidade absoluta']/df_grp['Quantidade']
        df_grp = df_grp.drop(columns=['Quantidade']).rename(columns={'Quantidade percentual' : 'Percentual', 'Quantidade absoluta' : 'Quantidade'})
        df_grp=df_grp[[dimensao,dimensao2,'Percentual','Quantidade']]
    else:
        df_grp=df_grp[[dimensao,'Quantidade']]

    return df_grp   

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
st.markdown("""# Detalhamento de perfil""")
st.write("---")
