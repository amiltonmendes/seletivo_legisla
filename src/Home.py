import streamlit as st
import pandas as pd
import numpy as np


################################## Configurações de página ####################################
st.set_page_config(
    page_title="Processo seletivo Legisla",
    layout="wide",
)

################################## Header ######################################################
st.markdown("""# Apresentação""")
st.write("---")
st.markdown("""No menu à esquerda serão encontrados dois painéis:
 * **Comparativo de Estados** : com informações da distribuição de orçamento e número de assessores de forma a permitir a comparação de diferentes métricas entre estados;
 * **Detalhamento de perfil por estado** : com informações da distribuição de orçamento e número de assessores para a análise de diferentes métricas em um estado selecionado.""")

