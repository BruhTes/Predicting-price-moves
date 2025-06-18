import os
import pandas as pd
from src.indicators import add_technical_indicators
from src.pynance_metrics import get_metrics_for_ticker

RAW_PATH = 'data/raw/yfinance'
OUTPUT_PATH = 'data/processed'
os.makedirs(OUTPUT_PATH, exist_ok=True)

files = [f for f in os.listdir(RAW_PATH) if f.endswith('.csv')]

for file in files:
    ticker = file.split('_')[0]  # AAPL_historical_data.csv -> AAPL
    print(f"\nProcessing {ticker}...")

    df = pd.read_csv(f"{RAW_PATH}/{file}")
    df = add_technical_indicators(df)
    df.to_csv(f"{OUTPUT_PATH}/{ticker}_indicators.csv", index=False)

    try:
        df_metrics, vol, sharpe = get_metrics_for_ticker(ticker)
        df_metrics.to_csv(f"{OUTPUT_PATH}/{ticker}_metrics.csv")
        print(f"✅ {ticker}: Vol={vol:.2f}, Sharpe={sharpe:.2f}")
    except Exception as e:
        print(f"⚠️ PyNance failed for {ticker}: {e}")