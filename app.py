# app.py (skeleton)
import streamlit as st
import pandas as pd
from utils import load_demo_clients, load_demo_transactions, load_demo_returns
import pages
import commentary

st.set_page_config(page_title="GAIA (Skeleton Demo)", layout="wide")
st.title("GAIA  Generative AI Investment Analytics (Skeleton Demo)")
st.caption("This public demo uses synthetic data and placeholder prompts. Replace with your own data & private prompts in production.")

clients = load_demo_clients()
client_names = clients["client_name"].tolist()
selected_client = st.sidebar.selectbox("Select Client", client_names)
model_option = st.sidebar.selectbox("Choose a model", ["demo-llm-small", "demo-llm-large"])

tabs = ["Overview", "Portfolio", "Commentary"]
selected_tab = st.sidebar.radio("Navigate", tabs)

txns = load_demo_transactions()
rets = load_demo_returns()

if selected_tab == "Overview":
    pages.render_overview(selected_client, txns, rets)
elif selected_tab == "Portfolio":
    pages.render_portfolio(selected_client, txns, rets)
else:
    text = commentary.generate_commentary(
        client=selected_client,
        strategy="Demo Strategy",
        model_name=model_option,
        context={"top_holdings":["AAPL","MSFT","NVDA"], "period_return":"1.2%", "benchmark_return":"0.9%"}
    )
    pages.render_commentary(selected_client, text)
