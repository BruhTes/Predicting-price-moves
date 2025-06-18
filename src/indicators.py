import pandas as pd
import pandas_ta as ta  

def add_technical_indicators(df: pd.DataFrame) -> pd.DataFrame:
    # SMA (Simple Moving Average)
    df['SMA_20'] = ta.sma(df['Close'], length=20)
    
    # RSI (Relative Strength Index)
    df['RSI_14'] = ta.rsi(df['Close'], length=14)
    
    # MACD (Moving Average Convergence Divergence)
    macd = ta.macd(df['Close'])
    df = pd.concat([df, macd], axis=1)
    
    return df
