import os
import pandas as pd
from src.sentiment import score_news_sentiment
from src.correlation import compute_daily_returns, aggregate_daily_sentiment, correlate_sentiment_returns

TICKERS = ['AAPL', 'AMZN', 'GOOG', 'META', 'MSFT', 'NVDA', 'TSLA']
news_df = pd.read_csv('data/news/cleaned_news.csv')
news_df['Date'] = pd.to_datetime(news_df['Date']).dt.date
news_df = score_news_sentiment(news_df)

for ticker in TICKERS:
    print(f"\nAnalyzing {ticker}...")
    news = news_df[news_df['Ticker'] == ticker]
    sentiment_daily = aggregate_daily_sentiment(news)

    stock_df = pd.read_csv(f"data/yfinance/{ticker}_historical_data.csv")
    stock_df['Date'] = pd.to_datetime(stock_df['Date']).dt.date
    returns = compute_daily_returns(stock_df)

    corr, merged = correlate_sentiment_returns(sentiment_daily, returns)
    merged.to_csv(f"data/processed/{ticker}_sentiment_correlation.csv", index=False)
    print(f"✅ Correlation for {ticker}: {corr:.4f}")