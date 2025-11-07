import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# 1️⃣ Leitura dos dados
# ==============================
st.set_page_config(page_title="Comparativo Despesa Total / PIB", page_icon="📊", layout="centered")

st.title("📊 Comparativo de Despesa Total / PIB por Estado")

# Upload do arquivo CSV
st.sidebar.header("📂 Importar dados")
uploaded_file = st.sidebar.file_uploader("Envie seu arquivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # ==============================
    # 2️
