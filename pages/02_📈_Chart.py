import streamlit as st

st.title("Charts")

symbol = st.sidebar.text_input("Stock symbol:", placeholder="AAPL")

if symbol:
    st.write(symbol)

