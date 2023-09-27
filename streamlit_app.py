from scraping import key_points
from plotly_chart import candlestick_maker
import streamlit as st

#Input
ticker = st.text_input("Enter the ticker: ", 'ITC')

#Keypoints
col1, col2, col3, col4 = st.columns(4)
col1.metric("Market Cap", f"{key_points(ticker)['market_cap']}")
col1.metric("PE", f"{key_points(ticker)['pe']}")
col1.metric("ROCE", f"{key_points(ticker)['roce']}")
col1.metric("ROE", f"{key_points(ticker)['roe']}")


#Candlestick chart
st.plotly_chart(candlestick_maker(ticker))

key_points = key_points(ticker)

print(key_points)
