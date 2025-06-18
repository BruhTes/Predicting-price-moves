import pandas as pd
from scipy.stats import pearsonr

def compute_daily_returns(df: pd.DataFrame) -> pd.DataFrame:
    df['Return'] = df['Close'].pct_change()
    return df[['Date', 'Return']].dropna()

def aggregate_daily_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(['Date']).agg({'Sentiment': 'mean'}).reset_index()

def correlate_sentiment_returns(sentiment_df, returns_df):
    merged = pd.merge(sentiment_df, returns_df, on='Date')
    corr, _ = pearsonr(merged['Sentiment'], merged['Return'])
    return corr, merged
