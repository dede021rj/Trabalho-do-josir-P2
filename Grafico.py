import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# 1️⃣ Leitura dos dados
# ==============================
caminho_csv = "/content/bq-results-20251105-191211-1762369940755.csv"
df = pd.read_csv(caminho_csv)

# ==============================
# 2️⃣ Título do app
# ==============================
st.title("📊 Comparativo de Despesa Total / PIB por Estado")

# ==============================
# 3️⃣ Seleção dos filtros
# ==============================
estados = df["sigla_uf"].unique()
anos = sorted(df["ano"].unique())

estado1 = st.selectbox("Selecione o primeiro estado:", estados, index=0)
estado2 = st.selectbox("Selecione o segundo estado:", estados, index=1)
ano = st.selectbox("Selecione o ano:", anos, index=len(anos)-1)



df_filtrado = df[(df["sigla_uf"].isin([estado1, estado2])) & (df["ano"] == ano)]

if df_filtrado.empty:
    st.warning("⚠️ Não há dados disponíveis para essa combinação de estados e ano.")
else:
    
    
    
    fig, ax = plt.subplots(figsize=(8, 4))
    cores = ["#1f77b4", "#ff7f0e"]

    barras = ax.bar(df_filtrado["sigla_uf"], df_filtrado["despesa_total_pib"] * 100, color=cores)

    
    for i, v in enumerate(df_filtrado["despesa_total_pib"]):
        ax.text(i, v * 100 + 0.02, f"{v * 100:.2f}%", ha="center", fontweight="bold")

    ax.set_title(f"Percentual da Despesa Total em relação ao PIB ({ano})", fontsize=14, pad=15)
    ax.set_xlabel("Estado")
    ax.set_ylabel("Despesa Total / PIB (%)")

    st.pyplot(fig)

    
    
    
    st.write("### 🔢 Dados utilizados")
    st.dataframe(df_filtrado[["sigla_uf", "ano", "despesa_total_pib"]])
