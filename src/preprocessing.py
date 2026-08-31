import pandas as pd
import numpy as np

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove coluna Id, duplicatas e cria target binario."""
    df_clean = df.copy()
    if 'Id' in df_clean.columns:
        df_clean = df_clean.drop(columns=['Id'])
    df_clean = df_clean.drop_duplicates().reset_index(drop=True)
    df_clean['quality_label'] = (df_clean['quality'] >= 7).astype(int)
    return df_clean

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """Cria features físico-químicas derivadas."""
    df_feat = df.copy()
    df_feat['bound_sulfur_dioxide'] = df_feat['total sulfur dioxide'] - df_feat['free sulfur dioxide']
    df_feat['acidity_ratio'] = df_feat['fixed acidity'] / (df_feat['volatile acidity'] + 1e-5)
    df_feat['free_sulfur_ratio'] = df_feat['free sulfur dioxide'] / (df_feat['total sulfur dioxide'] + 1e-5)
    return df_feat
