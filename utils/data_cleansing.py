# Replace NaNs to values minimizing distortion
import pandas as pd, numpy as np
def ReplaceNaNs(df):
    # Replace NaN on numeric column to average value
    df_clean = df.fillna(df.median())
    # Replace NaN on non-numeric column to str 'NaN'
    df_clean = df_clean.fillna('NaN')
    return df_clean

