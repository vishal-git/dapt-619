"""What should the raw data look like? Run from the repo root:  pytest -v tests/test_raw_data.py"""
import pytest
from cleaning import load_raw


@pytest.fixture(scope="module")
def raw():
    return load_raw()


# example 1: a test that passes
def test_churn_is_binary(raw):
    assert set(raw["churn"].unique()) <= {0, 1}


# example 2: a test that fails, and says how badly in its message
def test_customer_id_unique(raw):
    n = raw["customer_id"].is_duplicated().sum()
    assert n == 0, f"{n} rows share a customer_id"


# step 1: ages are plausible
# --

# step 2: charges make sense
# --

# step 3: category columns only contain the labels you expect (try @pytest.mark.parametrize)
# --

# step 4: your own idea
# --
