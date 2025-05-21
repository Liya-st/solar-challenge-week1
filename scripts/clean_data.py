import pandas as pd



def clean_data(df):
    negative_cols = ['GHI', 'DNI', 'DHI']
    for col in negative_cols:
        if col in df.columns:
            median_value = df[df[col] >= 0][col].median()
            df[col] = df[col].apply(lambda x: median_value if x < 0 else x)
        else:
            print(f"Column '{col}' not found in dataframe.")
    return df.reset_index(drop=True)

