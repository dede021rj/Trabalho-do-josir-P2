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
    # 2️⃣ Filtros interativos
    # ==============================
    estados = sorted(df["sigla_uf"].unique())
    anos = sorted(df["ano"].unique())

    st.sidebar.header("⚙️ Filtros")
    estado1 = st.sidebar.selectbox("Selecione o primeiro estado:", estados, index=0)
    estado2 = st.sidebar.selectbox("Selecione o segundo estado:", estados, index=1)
    ano = st.sidebar.selectbox("Selecione o ano:", anos, index=len(anos) - 1)

    # ==============================
    # 3️⃣ Filtragem dos dados
    # ==============================
    df_filtrado = df[(df["sigla_uf"].isin([estado1, estado2])) & (df["ano"] == ano)]

    if df_filtrado.empty:
        st.warning("⚠️ Não há dados disponíveis para essa combinação de estados e ano.")
    else:
        # ==============================
        # 4️⃣ Gráfico comparativo
        # ==============================
        fig, ax = plt.subplots(figsize=(8, 4))
        cores = ["#1f77b4", "#ff7f0e"]

        barras = ax.bar(df_filtrado["sigla_uf"], df_filtrado["despesa_total_pib"] * 100, color=cores)

        # Adiciona rótulos de valores
        for i, v in enumerate(df_filtrado["despesa_total_pib"]):
            ax.text(i, v * 100 + 0.02, f"{v * 100:.2f}%", ha="center", fontweight="bold")

        ax.set_title(f"Percentual da Despesa Total em relação ao PIB ({ano})", fontsize=14, pad=15)
        ax.set_xlabel("Estado")
        ax.set_ylabel("Despesa Total / PIB (%)")

        st.pyplot(fig)

        # ==============================
        # 5️⃣ Exibição dos dados numéricos
        # ==============================
        st.write("### 🔢 Dados utilizados")
        st.dataframe(df_filtrado[["sigla_uf", "ano", "despesa_total_pib"]])

        # ==============================
        # 6️⃣ Texto automático de interpretação (extra)
        # ==============================
        valores = dict(zip(df_filtrado["sigla_uf"], df_filtrado["despesa_total_pib"] * 100))
        if len(valores) == 2:
            uf1, uf2 = valores.keys()
            v1, v2 = valores.values()
            dif = abs(v1 - v2)
            maior = uf1 if v1 > v2 else uf2
            st.info(
                f"📈 Em {ano}, o estado **{maior}** apresentou o maior percentual de despesa em relação ao PIB "
                f"({max(v1, v2):.2f}%), superando o outro estado em aproximadamente **{dif:.2f} pontos percentuais**."
            )

else:
    st.warning("👈 Envie um arquivo CSV para começar a análise.")
