import pandas as pd
from scipy.stats import zscore


def remove_outliers(df: pd.DataFrame, columns: list, flags) -> pd.DataFrame:
    for col in columns:
        df.loc[flags, col] = df[col].median()
    return df
