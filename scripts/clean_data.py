import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:


    if 'Comments' in df.columns:
        df = df.drop(columns=['Comments'])

    negative_cols = ['GHI', 'DNI', 'DHI']
    for col in negative_cols:
        df = df[df[col] >= 0]

    df = df.reset_index(drop=True)

    return df
