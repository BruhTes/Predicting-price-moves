import pynance as pn
import pandas as pd

def get_metrics_for_ticker(ticker: str) -> tuple[pd.DataFrame, float, float]:
    asset = pn.Asset(ticker)
    df_metrics = asset.history(start='2023-01-01', end='2024-01-01')
    volatility = asset.volatility()
    sharpe = asset.sharpe()
    return df_metrics, volatility, sharpe