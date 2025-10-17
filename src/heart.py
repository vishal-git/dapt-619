import pandas as pd


def load_heart_dataframe():
    return pd.read_csv("data/raw/heart.csv")


def test_load_heart_dataframe_shape():
    df = load_heart_dataframe()
    assert df.shape == (918, 12)


def test_load_heart_dataframe_no_nulls():
    df = load_heart_dataframe()
    assert df.isnull().sum().sum() == 0


def test_missing_column():
    df = load_heart_dataframe()
    assert "heart_disease" in df.columns
