import pandas as pd

def calculate_headline_length(df: pd.DataFrame, text_col: str = "headline") -> pd.DataFrame:
    """
    Adds a column with character length of each headline.
    
    Args:
        df (pd.DataFrame): DataFrame with headline text.
        text_col (str): Column name containing text.
        
    Returns:
        pd.DataFrame: Original DataFrame with an added column `headline_length`.
    """
    df = df.copy()
    df["headline_length"] = df[text_col].astype(str).apply(len)
    return df
