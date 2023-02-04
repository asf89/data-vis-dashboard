import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import copy as cp
from PIL import Image

st.title("Detetive dos Cartéis de Combustíveis")
image_comb_rob = Image.open("assets/combustivel_rob.jpeg")
st.image(image_comb_rob)

st.write("Esta _dashboard_ procura mostrar as diferenças de preços entre diferentes bandeiras em diferentes municípios do Brasil a fim de detectar possíveis cartéis.")

st.write("## **Variação de preço por município**")

df = pd.read_csv("data/Longelat.csv")
es = cp.deepcopy(df)

es_opt = st.selectbox("Selecione o Estado:", es["Estado - Sigla"].unique())
fig_es = px.box(
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

fig_es2 = px.violin(
    es.query("`Estado - Sigla` == @es_opt"),
    x="Municipio",
    y="Valor de Venda",
    labels={
        "Municipio": "<b>Município</b>",
        "Valor de Venda": "<b>Preço de Venda</b>"
    },
    color="Municipio"
)

st.plotly_chart(fig_es, theme=None, use_container_width=True)
st.plotly_chart(fig_es2, theme=None, use_container_width=True)

st.write("## **Variação de preço por bandeira no município**")

mu_opt = st.text_input("Digite um município:")

fig_mu = go.Figure(data = go.Violin(
    x=es.query("Municipio == @mu_opt.upper()")["Bandeira"],
    y=es.query("Municipio == @mu_opt.upper()")["Valor de Venda"],
    box_visible=True,
    meanline_visible=True,
    opacity=.6,
    box={
        "fillcolor": "yellow"
    }
))

fig_mu.update_layout(title_text=f"<b>Variação de preço por bandeira em {mu_opt}</b>")
fig_mu.update_xaxes(title_text="<b>Bandeira</b>")
fig_mu.update_yaxes(title_text="<b>Preço de Venda</b>")

st.plotly_chart(fig_mu, theme=None, use_container_width=True)
