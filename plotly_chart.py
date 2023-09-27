import plotly.graph_objects as go
from stock_data import get_data

# ticker = "ITC"
# fig = go.Figure(
#     data = [
#         go.Candlestick(
#             x = get_data(ticker)['date'],
#             open = get_data(ticker)['open'],
#             close = get_data(ticker)['close'],
#             high = get_data(ticker)['high'],
#             low = get_data(ticker)['low']
#         )
#     ]
# )

# fig.update_layout(xaxis_rangeslider_visible=False)
# fig.show()

def candlestick_maker(ticker):
    fig = go.Figure(
    data = [
        go.Candlestick(
            x = get_data(ticker)['date'],
            open = get_data(ticker)['open'],
            close = get_data(ticker)['close'],
            high = get_data(ticker)['high'],
            low = get_data(ticker)['low']
        )
    ])
    fig.update_layout(xaxis_rangeslider_visible=False)
    return fig