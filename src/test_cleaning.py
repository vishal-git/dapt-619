# Demo 2b (complete version): testing data code with a fixture.
# Run:  pytest -v src/test_cleaning.py     -> 3 passed
import pandas as pd
import pytest
from cleaning import clean_customers


@pytest.fixture
def raw():
    # a tiny, hand-made DataFrame: you know the right answer by looking at it
    return pd.DataFrame({"customer_id": [1, 1, 2],
                         "state": [" va", " va", "NC "]})


def test_removes_duplicates(raw):
    assert clean_customers(raw)["customer_id"].is_unique


def test_normalizes_state(raw):
    assert list(clean_customers(raw)["state"]) == ["VA", "NC"]


def test_does_not_modify_input(raw):
    before = raw.copy()
    clean_customers(raw)     # result not needed here
    pd.testing.assert_frame_equal(raw, before)
