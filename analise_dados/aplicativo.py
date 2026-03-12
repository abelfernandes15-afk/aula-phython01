import streamlit as st
import pandas as pd
import plotly as px

st.title('dashboard de funcinarios')

df= pd.read_csv('novos_dados.csv')
st.subheader('tabela de dados ')
st. dataframe(df)

departamento= st.selectbox('selecione departamento',df['departamento'].unique())
df_diltrado= df[df]('departamento') == departamento
st.subheader('dados filtrados')
st.dataframe(df)

barra= px.bar(
    df_diltrado,
    x = 'nome completo',
    y= 'salario mensal br',
    color = 'nome completo',
    title= ' funcionarios'
)
st.plotly_chart(barra)