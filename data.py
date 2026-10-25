import yfinance as yf
import pandas as pd


def load(ticker, period="3y"):
    """Download daily close prices for a ticker."""
    df = yf.download(ticker, period=period, auto_adjust=True, progress=False)
    if isinstance(df.columns, pd.MultiIndex):
        df = df.droplevel(1, axis=1)
    return df[["Close"]].dropna()


if __name__ == "__main__":
    df = load("AAPL")
    print(df.tail())
    