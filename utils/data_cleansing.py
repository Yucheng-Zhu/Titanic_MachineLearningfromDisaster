# Replace NaNs to values minimizing distortion
import pandas as pd, numpy as np
def ReplaceNaNs(df):
    # Replace NaN on numeric column to average value
    df_clean = df.fillna(df.median())
    # Replace NaN on non-numeric column to str 'NaN'
    df_clean = df_clean.fillna('NaN')
    return df_clean

def SeparateNumericAndNonNumericFeatures(df_train, drops=None):
    import numpy as np
    numeric_types = (np.number, bool)
    if drops == None:
        drops = []
    df_train_forSeparation = df_train.drop(columns=drops)
    features_numeric = \
        df_train_forSeparation.select_dtypes(numeric_types).columns
    
    features_non_numeric = \
        df_train_forSeparation.select_dtypes(exclude=numeric_types).columns
    
    assert len(features_numeric) + len(features_non_numeric) == \
            len(df_train.columns) - len(drops)
    return features_numeric, features_non_numeric
    
