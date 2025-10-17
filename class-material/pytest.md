1. Create a new file called `addition.py`.
2. Write the following code into it:
```python
def add_number(a, b):
    return a + b

print(add_number(3, 5))
```
3. Run the script using `python addition.py` and show that it returns the correct output. 
4. Add a test to this function.
```python
def test_add_number():
    assert add_number(3, 5) == 8
```
5. Run the code using `pytest -q` and show how it passes. (Confirm the run command.)
6. It won't run—we need to install `pytest`. Activate the virtual environment first and then install it: `pip install pytest`.
7. Add a few more tests: 
```python
def test_add_number():
    assert add_number(3, 5) == 8
    assert add_number(-1, 1) == 0
    assert add_number(0, 0) == 0
```
8. Run again and check the output. All tests pass.
9. Change `return a + b` to `return a - b` to indicate a typo, and then re-run the tests to show how two of them will fail. But one will pass!
10. Exercise
    1. Create a new Python virtual environment for this exercise or reuse the one that we created in the previous section.
    2. Install `pandas`.
    3. Write a simple function to load `heart.csv` file into a Pandas dataframe.
    4. Write a test to verify that the dataframe contains twelve columns.
    5. Check if you already have `pytest` in the virtual environment. Install it if needed.
    6. Run the test and check the results. The test should pass.
    7. Write another test to verify that there are no null values in any columns.
    8. Run the test and check the results. (This test should pass.)
    9. Write another test to verify that the column `heart_disease` is present.
    10. Run the test and check the results. Inspect the results and figure out why the test failed.
