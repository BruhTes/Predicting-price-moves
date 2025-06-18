from textblob import TextBlob
import pandas as pd

def get_sentiment(text: str) -> float:
    return TextBlob(text).sentiment.polarity

def score_news_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    df['Sentiment'] = df['Headline'].apply(get_sentiment)
    return df
