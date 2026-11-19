import pandas as pd

# run from the repo root:  pytest -v src/heart_tutorial.py


# step 1: write a function that loads data/heart.csv into a DataFrame
def load_heart(path="data/heart.csv"):
    # --
    pass


# ---------- Part A: does the file look the way we expect? ----------

# step 2: test that the DataFrame has 12 columns
def test_has_twelve_columns():
    # --
    pass


# step 3: test that there are no null values in any column
# --


# step 4: test that the column "heart_disease" is present (read the error message!)
# --


# ---------- Part B: does the data make sense? (pick two) ----------

# step 5: Age is between 18 and 100
# --

# step 6: Sex only contains "M" or "F"
# --

# step 7: HeartDisease only contains 0 and 1
# --

# step 8: Cholesterol is greater than 0; count the bad rows and put the count in the assert message
#         hint: assert bad == 0, f"{bad} rows have Cholesterol <= 0"
# --
