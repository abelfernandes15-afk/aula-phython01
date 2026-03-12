import streamlit as st
import pandas as pd
import plotly.express as px

#CRIACAO DO TITULO
st.title('dashboard desempenho de alunos')

#CARREGAMENTO DOS DADOS
df= pd.read_csv('dados.csv')
st.subheader('tabela de dados ')
st. dataframe(df)

Curso = st.selectbox('selecione curso', df['curso'].unique())
df_filtrado = df[df]['Curso'] == Curso
st.subheader('dados filtrados')
st.write(df_filtrado)

# ELABORAÇAO DE GRAFICO
barra= px.bar(
    df_filtrado,
    x='aluno',
    y= 'nota',
    color= 'aluno',
    title= 'notas dos alunos'
)
st.plotly_chart(barra)