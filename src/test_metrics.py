# run from the repo root:  pytest -v src/test_metrics.py
import pytest
from metrics import percent_change


@pytest.mark.parametrize("old, new, expected", [
    (80, 100, 25.0),
    (100, 80, -20.0),
    (50, 50, 0.0),
    (-50, -25, 50.0),
])
def test_percent_change(old, new, expected):
    assert percent_change(old, new) == expected


def test_percent_change_float():
    assert percent_change(3, 3.3) == pytest.approx(10.0)


def test_percent_change_zero_old():
    with pytest.raises(ValueError):
        percent_change(0, 10)
