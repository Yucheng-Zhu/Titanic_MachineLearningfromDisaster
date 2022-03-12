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
    
# -- 'Embarked': C, Q, S -> 0.553571, 0.389610, 0.336957
def EncodeNumericalCategoricalVariables(
    df_train, 
    NumericalCategoricalVariableName,
    NameToCalculateResultRate=None,
    SurvivalRatesForAllCategories=None
):
    df_train_numericized = df_train.copy(deep=True)
    n = NumericalCategoricalVariableName
    
    Grouped = df_train.groupby(
        n
    ).sum()
    if SurvivalRatesForAllCategories is None:
        actual_name, total_name = NameToCalculateResultRate
        SurvivalRatesForAllCategories = \
            Grouped[actual_name] / Grouped[total_name]
    
    for i in Grouped.index:
        df_train_numericized.loc[
            df_train[n].values == i,
            n
        ] = SurvivalRatesForAllCategories[i]
    df_train_numericized[n] = \
        df_train_numericized[n].astype('float64')
    return df_train_numericized, SurvivalRatesForAllCategories
# df_train_numericized, SurvivalRatesForAllCategories = EncodeNumericalCategoricalVariables(
    # df_train_preparsed, 
    # 'Embarked',
    # NameToCalculateResultRate=('Survived','Count')
# )
# df_test_numericized, _ = EncodeNumericalCategoricalVariables(
    # df_test_preparsed, 
    # 'Embarked',
    # SurvivalRatesForAllCategories=SurvivalRatesForAllCategories
# )
# df_train_numericized.head(5)

