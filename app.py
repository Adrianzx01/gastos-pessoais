import streamlit as st
from src.api_client import get_usd_quotation

st.title("🤞 Gerenciador de Gastos - Expansão de Domínio")

st.header("Cotação em Tempo Real")
if st.button('Consultar Dólar Agora'):
    cotacao = get_usd_quotation()
    if cotacao:
        st.success(f"O Dólar está valendo: R$ {cotacao:.2f}")
    else:
        st.error("Erro ao buscar cotação.")

st.info("Nota: Esta é a versão Web para Deploy da ferramenta CLI de Gastos Pessoais.")
