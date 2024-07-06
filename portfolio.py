import pandas as pd
import yfinance as yf

# Define the portfolio
portfolio = {
    'AAPL': 10,   # 10 shares of Apple
    'GOOGL': 5,   # 5 shares of Alphabet (Google)
    'TSLA': 2,    # 2 shares of Tesla
    'AMZN': 1     # 1 share of Amazon
}

def fetch_stock_data(tickers):
    data = yf.download(tickers, period="1d", interval="1d")
    return data['Adj Close']

def calculate_portfolio_value(portfolio, prices):
    total_value = 0
    for ticker, shares in portfolio.items():
        total_value += shares * prices[ticker]
    return total_value

# Fetch the latest stock prices
tickers = list(portfolio.keys())
prices = fetch_stock_data(tickers)

# Calculate the portfolio value
portfolio_value = calculate_portfolio_value(portfolio, prices.iloc[0])

# Print the results
print("Stock Prices (Adjusted Close):")
print(prices)

print("\nPortfolio Value:")
print(f"${portfolio_value:.2f}")
