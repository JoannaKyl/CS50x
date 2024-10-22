import yfinance as yf
import cryptocompare as c
from flask import redirect, render_template, request, session

def stock_quote (symbol):
    try:
        stock =yf.Ticker(symbol)
        market_price = stock.info['currentPrice']
        return market_price
    except Exception:
        print("Symbol not found")
        return None


def crypto_quote(symbol):
    try:
        current_price =c.get_price(symbol,currency="USD")
        if current_price != 0:
            return current_price[symbol]["USD"]
    except Exception:
        print("Symbol not found")
        return None

