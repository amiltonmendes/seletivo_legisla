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
    df_grp = df_grp.sort_values(by=dimensao)   
    return df_grp

def get_dados_agrupados_soma(df,dimensao,dimensao2=None):
    df_grp = df.groupby([dimensao]).sum(numeric_only=True).reset_index()[[dimensao,'Orçamento disponível ']]
    if dimensao2!=None:
        df_parcial = df.groupby([dimensao,dimensao2]).sum(numeric_only=True).rename( columns = {'Orçamento disponível ' : 'Orçamento'}).reset_index()
        df_grp = df_grp.merge(df_parcial,how='inner',on=[dimensao])
        df_grp['Orçamento Relativo'] = 100*df_grp['Orçamento']/df_grp['Orçamento disponível ']
        df_grp=df_grp[[dimensao,dimensao2,'Orçamento Relativo','Orçamento']]
    else:
        df_grp=df_grp[[dimensao,'Orçamento disponível ']]
    df_grp = df_grp.sort_values(by=dimensao)   
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
st.markdown("""# Comparativo de Estados""")
st.write("---")
df=get_dados()

st.markdown('## 1.Cargos')
st.markdown('### 1.1. Quantidade ')
df_grp = get_dados_agrupados(df,'Estado ','Cargo ')
fig = px.bar(df_grp, y="Quantidade",x='Estado ',color='Cargo ')
fig.update_xaxes(categoryorder='category ascending')
st.plotly_chart(fig)

st.markdown('### 1.2. Orçamento ')
df_grp = get_dados_agrupados_soma(df,'Estado ','Cargo ')
fig = px.bar(df_grp, y="Orçamento",x='Estado ',color='Cargo ')
fig.update_xaxes(categoryorder='category ascending')
st.plotly_chart(fig)

st.markdown('## 2.Identidade de gênero')
st.markdown('### 2.1. Quantidade ')
df_grp = get_dados_agrupados(df,'Estado ','Identidade de gênero')
fig = px.bar(df_grp, y="Quantidade",x='Estado ',color='Identidade de gênero')
fig.update_xaxes(categoryorder='category ascending')
st.plotly_chart(fig)

st.markdown('### 2.2. Orçamento ')
df_grp = get_dados_agrupados_soma(df,'Estado ','Identidade de gênero')
fig = px.bar(df_grp, y="Orçamento",x='Estado ',color='Identidade de gênero')
fig.update_xaxes(categoryorder='category ascending')
st.plotly_chart(fig)


st.markdown('## 3.Cor')
st.markdown('### 3.1. Quantidade ')
df_grp = get_dados_agrupados(df,'Estado ','Cor')
fig = px.bar(df_grp, y="Quantidade",x='Estado ',color='Cor')
fig.update_xaxes(categoryorder='category ascending')
st.plotly_chart(fig)

st.markdown('### 3.2. Orçamento ')
df_grp = get_dados_agrupados_soma(df,'Estado ','Cor')
fig = px.bar(df_grp, y="Orçamento",x='Estado ',color='Cor')
fig.update_xaxes(categoryorder='category ascending')
st.plotly_chart(fig)



st.markdown('## 4.Partido')
st.markdown('### 4.1. Quantidade ')
df_grp = get_dados_agrupados(df,'Estado ','Partido')
fig = px.bar(df_grp, y="Quantidade",x='Estado ',color='Partido')
fig.update_xaxes(categoryorder='category ascending')
st.plotly_chart(fig)

st.markdown('### 4.2. Orçamento ')
df_grp = get_dados_agrupados_soma(df,'Estado ','Partido')
fig = px.bar(df_grp, y="Orçamento",x='Estado ',color='Partido')
fig.update_xaxes(categoryorder='category ascending')
st.plotly_chart(fig)