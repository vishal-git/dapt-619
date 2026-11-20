import pandas as pd
import pytest

# Copy this file into your pytest-demo folder (and heart.csv into pytest-demo/data/), then run:  pytest -v heart_tutorial.py
# Each test below is set up for you: replace its pytest.skip(...) line with your assert.
# Tests you haven't written yet show up as SKIPPED, so you always know which ones are left.


# step 1: write a function that loads data/heart.csv into a DataFrame (hint: pd.read_csv)
def load_heart(path="data/heart.csv"):
    # --
    pass  # replace this line with your code


# ---------- Part A: does the file look the way we expect? ----------

# step 2: the DataFrame has 12 columns (hint: df.shape is (rows, columns))
def test_has_twelve_columns():
    df = load_heart()
    pytest.skip("not written yet")  # replace this line with your assert


# step 3: there are no null values in any column (hint: df.isnull().sum().sum() counts them)
def test_no_nulls():
    df = load_heart()
    pytest.skip("not written yet")  # replace this line with your assert


# step 4: the column "heart_disease" is present (hint: df.columns); read the error message!
def test_has_heart_disease_column():
    df = load_heart()
    pytest.skip("not written yet")  # replace this line with your assert


# ---------- Part B: does the data make sense? (pick two) ----------

# step 5: Age is between 18 and 100 (hint: df["Age"].between(18, 100) gives True/False per row; .all() checks every row)
def test_age_in_range():
    df = load_heart()
    pytest.skip("not written yet")  # replace this line with your assert


# step 6: Sex only contains "M" or "F" (hint: compare set(df["Sex"]) with {"M", "F"})
def test_sex_values():
    df = load_heart()
    pytest.skip("not written yet")  # replace this line with your assert


# step 7: HeartDisease only contains 0 and 1
def test_target_is_binary():
    df = load_heart()
    pytest.skip("not written yet")  # replace this line with your assert


# step 8: Cholesterol and RestingBP are greater than 0; count the bad rows and put the count in the assert message
#         hint:  bad = (df["Cholesterol"] <= 0).sum()
#                assert bad == 0, f"{bad} rows have Cholesterol <= 0"
def test_cholesterol_positive():
    df = load_heart()
    pytest.skip("not written yet")  # replace this line with your code


def test_resting_bp_positive():
    df = load_heart()
    pytest.skip("not written yet")  # replace this line with your code (same idea as the test above)


# ---------- Stretch: one parametrized test instead of the two above ----------
# @pytest.mark.parametrize("col", ["Cholesterol", "RestingBP"])
# def test_measurement_positive(col):
#     ...
