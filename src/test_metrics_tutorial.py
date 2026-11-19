# Copy this file and src/metrics.py into your pytest-demo folder, then run:  pytest -v test_metrics_tutorial.py
import pytest
from metrics import percent_change


# step 1: use @pytest.mark.parametrize to test these cases in one test function
#         (80, 100) -> 25.0, (100, 80) -> -20.0, (50, 50) -> 0.0, (-50, -25) -> 50.0
# --


# step 2: test that percent_change(3, 3.3) is 10.0 (hint: floats are never exactly equal)
# --


# step 3: test that percent_change(0, 10) raises a ValueError
# --
