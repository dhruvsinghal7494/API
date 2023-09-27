from bs4 import BeautifulSoup
import requests

def key_points(ticker):
    html_text = requests.get(f"https://www.screener.in/company/{ticker}/consolidated/").text
    soup = BeautifulSoup(html_text, 'lxml')
    fundamentals = soup.find_all('span', class_='number')
    key_points = []
    for key_point in fundamentals:
        key_point = key_point.text
        key_points.append(key_point)
    market_cap = key_points[0]
    current_price = key_points[1]
    high = key_points[2]
    low = key_points[3]
    pe = key_points[4]
    book_value = key_points[5]
    divident_yeild = key_points[6]
    roce = key_points[7]
    roe = key_points[8]
    face_value = key_points[9]

    return {
        'market_cap': market_cap,
        'current_price': current_price,
        'high': high,
        'low': low,
        'pe': pe,
        'book_value': book_value,
        'dividend_yield': divident_yeild,
        'roce': roce,
        'roe': roe,
        'face_value': face_value
    }

# print(key_points("ITC")['pe'])