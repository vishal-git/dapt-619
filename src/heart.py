import pandas as pd
import pytest

# run from the repo root:  pytest -v src/heart.py


def load_heart(path="data/heart.csv"):
    return pd.read_csv(path)


# ---------- Part A: does the file look the way we expect? ----------

def test_has_twelve_columns():
    assert load_heart().shape[1] == 12


def test_no_nulls():
    assert load_heart().isnull().sum().sum() == 0


def test_has_heart_disease_column():
    # fails on purpose: read the error message to see the real column name
    assert "heart_disease" in load_heart().columns


# ---------- Part B: does the data make sense? ----------

def test_age_in_range():
    df = load_heart()
    assert df["Age"].between(18, 100).all()


def test_sex_values():
    assert set(load_heart()["Sex"]) <= {"M", "F"}


def test_target_is_binary():
    assert set(load_heart()["HeartDisease"]) <= {0, 1}


def test_cholesterol_positive():
    # fails on purpose: zeros are missing values in disguise
    df = load_heart()
    bad = (df["Cholesterol"] <= 0).sum()
    assert bad == 0, f"{bad} rows have Cholesterol <= 0"


def test_resting_bp_positive():
    df = load_heart()
    bad = (df["RestingBP"] <= 0).sum()
    assert bad == 0, f"{bad} rows have RestingBP <= 0"


# ---------- Stretch: one parametrized test instead of two ----------

@pytest.mark.parametrize("col", ["Cholesterol", "RestingBP"])
def test_measurement_positive(col):
    # fails on purpose for both columns: one test per column in the report
    df = load_heart()
    bad = (df[col] <= 0).sum()
    assert bad == 0, f"{bad} rows have {col} <= 0"
