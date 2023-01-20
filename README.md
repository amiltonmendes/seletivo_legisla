# Seletivo Legisla

## Metodologia

Os dados utilizados neste trabalho encontram-se disponibilizados no endereço  https://bit.ly/AnalistadeDadoseBI-PedroCampos. Após o download do referido arquivo, foi realizada uma etapa de análise exploratória de dados, onde, além de atividades de conhecimento dos dados, foram realizados procedimentos de limpeza e preparação de dados. 

Ato contínuo, foram construídos alguns painéis de forma a possibilitar a realização de algumas análises relacionadas ao objetivo do trabalho.

Todos os produtos entregues no âmbito deste trabalho foram desenvolvidos partir da utilização da linguagem de programação Python em conjunto com as bibliotecas pandas, numpy, streamlit e plotly. Os códigos encontram-se disponíveis em https://github.com/amiltonmendes/seletivo_legisla. 

## Análise exploratória de dados
O arquivo utilizado neste trabalho apresentou 73 registros e 9 colunas, quais sejam, “Nome do Assessor”, “Ano de ingresso no Congresso”, “Cargo”, “Idade que começou a trabalhar”, “Identidade de gênero”, “Partido” ,  “Cor” , “Estado”  e “Orçamento disponível”.

No que tange a qualidade de dados, observou-se problemas relacionados a utilização de caracteres não numéricos em campos numéricos, como nos campos “Ano de ingresso no Congresso”, “Idade que começou a trabalhar”.

Além disso, observou-se classes de Cor redundantes, como “Pardo” e “Parda” ou “Branca” e “Pessoa Branca”. 

Embora tenham sido criadas rotinas para a harmonização e correção dos problemas acima descritos, recomenda-se a melhoria nos processos de captura dos dados.

Ainda em relação à qualidade de dados, identificou-se assessores com informações de orçamento discrepantes das demais observações do conjunto. São os assessores identificados pelos nomes Assessor 12, Assessor 51 e Assessor 11, com, respectivamente, R$ 760.505.847, R$ 658.672.302 e R$ 652.177.271 de orçamento disponível. 

## Demais Informações
Todos os códigos produzidos no âmbito deste projeto encontram-se na pasta src.

O jupyter notebook 01 AED.ipynb contém a análise exploratória de dados preliminar e rotinas de preparação de dados.

Os dashboards construídos utilizam as bibliotecas pandas, streamlit, numpy e plotly e podem ser visualizados a partir do seguinte comando, executado da raiz deste projeto: streamlit run ./src/Home.py
