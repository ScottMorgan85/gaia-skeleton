# pages.py (skeleton)
import streamlit as st
import pandas as pd

def render_overview(client_name: str, transactions: pd.DataFrame, returns: pd.DataFrame):
    st.subheader(f"Overview  {client_name}")
    c1, c2 = st.columns(2)
    with c1:
        st.write("Recent Transactions (demo)")
        st.dataframe(transactions.head(5), use_container_width=True, hide_index=True)
    with c2:
        st.write("Recent Returns (demo)")
        st.dataframe(returns.head(5), use_container_width=True, hide_index=True)

def render_portfolio(client_name: str, transactions: pd.DataFrame, returns: pd.DataFrame):
    st.subheader(f"Portfolio  {client_name}")
    st.write("This is a skeleton view. Replace with your analytics & charts.")
    st.dataframe(transactions, use_container_width=True, hide_index=True)

def render_commentary(client_name: str, commentary_text: str):
    st.subheader(f"Commentary  {client_name}")
    st.markdown(commentary_text)
