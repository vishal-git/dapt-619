"""Tests for clean(). Run from the repo root:  pytest -v tests/test_cleaning.py"""
import polars as pl
import pytest
from cleaning import clean


@pytest.fixture
def tiny():
    # step 1: a few hand-made rows that contain each problem you found
    return pl.DataFrame({
        "customer_id": ["A", "A", "B"],
        "churn": [1, 1, 0],
        # --
    })


# step 2: one test per fix, e.g. duplicates are removed
# --

# step 3: clean() does not modify its input
# --
