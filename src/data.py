import streamlit as st
import yfinance as yf


@st.cache
def get_stock(symbol):
    return yf.Ticker(symbol.upper())
