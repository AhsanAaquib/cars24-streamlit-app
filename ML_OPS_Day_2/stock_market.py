import streamlit as st
import pandas as pd
import numpy as np

import yfinance as yf

st.title("Stock Market Analysis!")


# st.header("Select a stock to analyze")
# st.subheader("Enter the stock ticker symbol below:")

# st.write("This app allows you to analyze stock data using the yfinance library.")


# let's see the examples of widgets

# if st.checkbox("Show examples of widgets"):
#     st.write("This is a checkbox widget. You can check or uncheck it.")
#     st.write("This is a radio button widget. You can select one option from the list below:")
#     st.write("This is a selectbox widget. You can select one option from the list below:")
#     st.write("This is a multiselect widget. You can select multiple options from the list below:")
#     st.write("This is a slider widget. You can select a value from the range below:")
#     st.write("This is a text input widget. You can enter text in the box below:")
#     st.write("This is a number input widget. You can enter a number in the box below:")
#     st.write("This is a date input widget. You can select a date from the calendar below:")
#     st.write("This is a time input widget. You can select a time from the clock below:")
#     st.write("This is a file uploader widget. You can upload a file from your computer:")
#     st.write("This is a color picker widget. You can select a color from the color picker below:")
#     st.write("This is a button widget. You can click the button below:")

start_date = st.date_input("Start date", pd.to_datetime("2020-01-01"))

end_date = st.date_input("End date", pd.to_datetime("2023-10-01"))

symbol = "AAPL"

ticker_symbol = st.text_input("Enter the stock ticker symbol", "AAPL")

ticker_data = yf.Ticker(ticker_symbol)

ticker_df = ticker_data.history(start=start_date, end=end_date, period="1d")

st.dataframe(ticker_df)

st.write("### Closing Price vs Volume")

st.line_chart(ticker_df.Close, use_container_width=True) # Inside the libe chart, pass then series.

col1, col2 = st.columns(2)  

with col1:
    st.write("### Daily Closing Price Chart")
    st.line_chart(ticker_df.Close, use_container_width=True)

with col2:
    st.write("### Daily Volume Chart")
    st.line_chart(ticker_df.Volume, use_container_width=True)