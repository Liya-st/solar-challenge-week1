# Identify numeric columns
import numpy as np
from scipy import stats
def detect_outliers(df, numeric_cols):

    # Compute Z-scores and flag outliers (|Z| > 3)
    z_scores = np.abs(stats.zscore(df[numeric_cols]))
    outlier_flags = (z_scores > 3).any(axis=1)
    print(f"Number of outlier samples flagged: {outlier_flags.sum()}")
    return outlier_flags