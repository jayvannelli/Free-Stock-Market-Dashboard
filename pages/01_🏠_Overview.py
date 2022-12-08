import streamlit as st
import yfinance as yf

st.title("Overview")
symbol = st.sidebar.text_input("Stock symbol:", placeholder="AAPL")

if symbol:
    stock = yf.Ticker(symbol)
    info = stock.info

    st.write("---")
    st.title(f"{info['longName']} | ${info['symbol']}")

    c1, c2 = st.columns([2, 1])
    with c1:
        st.write(info['website'])
        st.write(f"{info['sector']} | {info['industry']}")

    with c2:
        st.image(info['logo_url'])

    st.subheader("Summary")
    st.write(info['longBusinessSummary'])

    st.write(info)
