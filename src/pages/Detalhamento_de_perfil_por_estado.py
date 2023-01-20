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
################################## Filtro #####################################################
#filtro = st.expander(':mag:Filtros')
col1, _ = st.columns(2)
selecao_estado = col1.selectbox(label=':mag: Estado',options= get_estados(),)
df=get_dados()
df_estado = df[df['Estado ']==selecao_estado]
st.write("---")

st.markdown('## 1. Quantidade de assessores')
col1, col2 = st.columns(2)
df_grp = get_dados_agrupados(df_estado,'Identidade de gênero')
#df_estado.groupby(['Identidade de gênero']).count().rename(columns={'Nome do Assessor' : 'Quantidade'}).reset_index()
col1.markdown('#### Por identidade de gênero ')
fig = px.bar(df_grp, y="Quantidade",x='Identidade de gênero')
col1.plotly_chart(fig)

df_grp = get_dados_agrupados(df_estado,'Cor')
col2.markdown('#### Por cor ')
fig = px.bar(df_grp, y="Quantidade",x='Cor')
col2.plotly_chart(fig)


st.markdown('## 2.Orçamento')
col1, col2 = st.columns(2)

col1.markdown('#### Por identidade de gênero ')
fig = px.box(df_estado, y="Orçamento disponível ",x='Identidade de gênero')
col1.plotly_chart(fig)

col2.markdown('#### Por cor ')
fig = px.box(df_estado, y="Orçamento disponível ",x='Cor')
col2.plotly_chart(fig)

st.markdown('## 3.Cargos')
st.markdown('### 3.1. Quantidade ')
col1, col2 = st.columns(2)
col1.markdown('#### Por identidade de gênero ')
df_grp = get_dados_agrupados(df_estado,'Identidade de gênero','Cargo ')
fig = px.bar(df_grp, y="Quantidade",x='Identidade de gênero',color='Cargo ')
col1.plotly_chart(fig)

col2.markdown('#### Por cor ')
df_grp = get_dados_agrupados(df_estado,'Cor','Cargo ')
fig = px.bar(df_grp, y="Quantidade",x='Cor',color='Cargo ')
col2.plotly_chart(fig)

st.markdown('### 3.2. Percentual ')
col1, col2 = st.columns(2)
col1.markdown('#### Por identidade de gênero ')
df_grp = get_dados_agrupados(df_estado,'Identidade de gênero','Cargo ')
fig = px.bar(df_grp, y="Percentual",x='Identidade de gênero',color='Cargo ')
col1.plotly_chart(fig)

col2.markdown('#### Por cor ')
df_grp = get_dados_agrupados(df_estado,'Cor','Cargo ')
fig = px.bar(df_grp, y="Percentual",x='Cor',color='Cargo ')
col2.plotly_chart(fig)

st.markdown('## 4.Partidos')
st.markdown('### 4.1. Quantidade ')
col1, col2 = st.columns(2)
col1.markdown('#### Por identidade de gênero ')
df_grp = get_dados_agrupados(df_estado,'Identidade de gênero','Partido')
fig = px.bar(df_grp, y="Quantidade",x='Identidade de gênero',color='Partido')
col1.plotly_chart(fig)

col2.markdown('#### Por cor ')
df_grp = get_dados_agrupados(df_estado,'Cor','Partido')
fig = px.bar(df_grp, y="Quantidade",x='Cor',color='Partido')
col2.plotly_chart(fig)

st.markdown('### 4.2. Percentual ')
col1, col2 = st.columns(2)
col1.markdown('#### Por identidade de gênero ')
df_grp = get_dados_agrupados(df_estado,'Identidade de gênero','Partido')
fig = px.bar(df_grp, y="Percentual",x='Identidade de gênero',color='Partido')
col1.plotly_chart(fig)

col2.markdown('#### Por cor ')
df_grp = get_dados_agrupados(df_estado,'Cor','Partido')
fig = px.bar(df_grp, y="Percentual",x='Cor',color='Partido')
col2.plotly_chart(fig)

st.markdown('## 5.Idade em que começou a trabalhar')
col1, col2 = st.columns(2)

col1.markdown('#### Por identidade de gênero ')
fig = px.box(df_estado, y="Idade que começou a trabalhar",x='Identidade de gênero')
col1.plotly_chart(fig)

col2.markdown('#### Por cor ')
fig = px.box(df_estado, y="Idade que começou a trabalhar",x='Cor')
col2.plotly_chart(fig)

st.markdown('## 6.Ano de ingresso no congresso')
col1, col2 = st.columns(2)

col1.markdown('#### Por identidade de gênero ')
fig = px.box(df_estado, y="Ano de ingresso no Congresso",x='Identidade de gênero')
col1.plotly_chart(fig)

col2.markdown('#### Por cor ')
fig = px.box(df_estado, y="Ano de ingresso no Congresso",x='Cor')
col2.plotly_chart(fig)