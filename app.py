import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import copy as cp

st.title("Fiscal dos Combustíveis")
st.write("Esta _dashboard_ procura mostrar as diferenças de preços entre diferentes localidades de Recife-PE a fim de detectar cartéis.")

st.write("## **Variação de preço por Município**")

df = pd.read_csv("data/Longelat.csv")
es = cp.deepcopy(df)

es_opt = st.selectbox("Selecione o Estado:", es["Estado - Sigla"].unique())
fig = px.box(
    es.query("`Estado - Sigla` == @es_opt"),
    x="Municipio",
    y="Valor de Venda",
    title="<b>Variação de preço por município</b>",
    labels={
        "Municipio": "<b>Município</b>",
        "Valor de Venda": "<b>Preço de Venda<b>"
    },
    color="Municipio",
    notched=True
)

st.plotly_chart(fig, theme=None, use_container_width=True)

st.write("## **Variação de preço por bandeira no município**")

mu_opt = st.text_input("Digite um município")

