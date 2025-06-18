# B5W1: Predicting Price Moves with News Sentiment

## Overview

Dive into real-world financial news and discover how headlines shape stock swings! In this project, you'll analyze sentiment scores from news headlines, calculate technical indicators, and link them to daily stock returns to explore the impact of news sentiment on market movements.

---

## Challenge Overview

This challenge centers on analyzing a large corpus of financial news data to uncover correlations between news sentiment and stock price moves. It is designed to develop your skills in Data Engineering, Financial Analytics, and Machine Learning Engineering—just like in a fast-paced, real-world financial analytics environment.

---

## Business Objective

Nova Financial Solutions aims to enhance its predictive analytics to boost forecasting accuracy and operational efficiency. Your mission is to:

- **Sentiment Analysis:** Quantify the emotional tone of financial news headlines using NLP.
- **Correlation Analysis:** Establish statistical links between news sentiment and stock price changes.
- **Strategic Recommendations:** Use insights to suggest actionable investment strategies based on news sentiment and price movement relationships.

---

## Dataset Overview

**Financial News and Stock Price Integration Dataset (FNSPID)**

- **headline:** News article title.
- **url:** Link to the full article.
- **publisher:** Article author/organization.
- **date:** Publication date and time (UTC-4).
- **stock:** Ticker symbol (e.g., AAPL).

Additionally, you will use historical stock price data (Open, High, Low, Close, Volume).

---

## Team

- **Facilitator:** Mahlet
- **Members:** Kerod, Rediet, Rehmet

---

## Key Dates

- **Challenge Introduction:** Wed, 28 May 2025, 8:00 AM UTC
- **Interim Submission:** Fri, 30 May 2025, 8:00 PM UTC
- **Final Submission:** Tue, 03 June 2025, 8:00 PM UTC

---

## Communication & Support

- **Slack Channel:** #all-week1
- **Office Hours:** Mon–Fri, 08:00–15:00 UTC (Zoom)

---

## Learning Objectives

By the end of this project, you will:

- Set up a reproducible Python data science environment with GitHub integration.
- Perform EDA on text and time series data.
- Compute technical indicators (MA, RSI, MACD) using TA-Lib and PyNance.
- Run sentiment analysis on news headlines.
- Measure correlations between sentiment and daily returns.
- Document findings in a publication-style report.

---

## Project Structure

```
.github/
└── workflows/
    └── unittests.yml
data/
├── processed/
└── raw/
    └── yfinance/
        ├── AAPL_historical_data.csv
        ├── AMZN_historical_data.csv
        ├── GOOG_historical_data.csv
        ├── META_historical_data.csv
        ├── MSFT_historical_data.csv
        ├── NVDA_historical_data.csv
        ├── TSLA_historical_data.csv
        └── raw_analyst_ratings.csv
.vscode/
    └── settings.json
src/
    └── __init__.py
notebooks/
    ├── __init__.py
    └── README.md
tests/
    └── __init__.py
scripts/
    ├── __init__.py
    └── README.md
.gitignore
requirements.txt
README.md
```

---

## Project Planning & Tasks

### Task 1: Git and GitHub

- Set up Python environment and version control (Git, GitHub)
- Establish CI/CD (unit tests)
- **Deliverables:** 
  - Dev environment
  - Commit frequently with descriptive messages
  - Use branches (e.g., `task-1`)
  - EDA: Descriptive stats, article count by publisher, date analysis, topic modeling, time series and publisher analysis

### Task 2: Quantitative Analysis

- Load and prepare stock price data
- Calculate technical indicators with TA-Lib (MA, RSI, MACD)
- Use PyNance for financial metrics
- Visualize findings
- **Deliverables:** 
  - New branch `task-2`
  - Data preparation, calculation of indicators, visualizations

### Task 3: Correlation Analysis

- Align news and stock data by date
- Sentiment analysis on headlines (TextBlob, NLTK)
- Calculate daily stock returns
- Compute and visualize correlation between sentiment and returns
- **Deliverables:** 
  - New branch `task-3`
  - Data preparation, sentiment scoring, returns calculation, correlation analysis

---

## Minimum Essential To Do

- Create a GitHub repository and follow the folder structure above
- Use branches for each task (`task-1`, `task-2`, `task-3`)
- Commit work at least three times per day
- Merge changes via Pull Requests

---

## Tutorials & References

- [TA-Lib Documentation](https://mrjbq7.github.io/ta-lib/)
- [PyNance Documentation](https://pynance.readthedocs.io/en/latest/)
- [TextBlob Sentiment Analysis](https://textblob.readthedocs.io/en/dev/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Seaborn & Matplotlib for Visualization](https://seaborn.pydata.org/)

---

## Other Considerations

- Normalize timestamps and ensure data integrity
- Use clear, well-documented code
- Share references and learning resources with your team

---

## Acknowledgements

This project is inspired by real-world challenges in financial data analytics. Special thanks to Nova Financial Insights for the challenge framework and dataset.

---
