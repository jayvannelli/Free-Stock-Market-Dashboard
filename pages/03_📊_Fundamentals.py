import streamlit as st
import yfinance as yf


if 'symbol' in st.session_state:
    symbol = st.sidebar.text_input("Stock symbol:", value=st.session_state['symbol'])
else:
    symbol = st.sidebar.text_input("Stock symbol:", placeholder="AAPL")


@st.cache(allow_output_mutation=True)
def get_data(_stock):
    cash_flow = _stock.quarterly_cashflow
    fin = _stock.financials
    bal_sheet = _stock.balance_sheet
    return cash_flow, fin, bal_sheet


def main():

    if symbol:
        st.title(f"{symbol.upper()} Fundamentals")
        stock = yf.Ticker(symbol)

        cash_flow, financials, balance_sheet = get_data(stock)

        st.write(cash_flow, financials, balance_sheet)


if __name__ == "__main__":
    main()