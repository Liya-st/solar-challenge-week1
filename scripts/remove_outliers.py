import pandas as pd
from scipy.stats import zscore

def remove_outliers_iqr(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        original_size = df.shape[0]
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
        print(f"{col}: Removed {original_size - df.shape[0]} outliers.")
    return df.reset_index(drop=True)

def remove_zscore(df: pd.DataFrame, columns: list, threshold: float = 3.0) -> pd.DataFrame:
    z_scores = df[columns].apply(zscore)
    mask = (abs(z_scores) < threshold).all(axis=1)
    removed = df.shape[0] - mask.sum()
    print(f"Z-score: Removed {removed} outliers.")
    return df[mask].reset_index(drop=True)
