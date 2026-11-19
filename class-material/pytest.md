# Unit testing with pytest

## Demo 1: `add_number` (complete version: `src/addition.py`)

1. Activate the course environment (`conda activate dapt619`); pytest is already installed from `requirements.txt`. Confirm with `pytest --version`.
2. Make a new folder for this demo, next to the `dapt-619` repo (not inside it, so the repo stays untouched):

   ```bash
   cd ..              # from dapt-619/ up to your course folder
   mkdir pytest-demo
   cd pytest-demo
   ```

   Open this folder in VS Code (**File → Open Folder**) and use VS Code's Git Bash terminal from here on. A new terminal starts outside the environment, so run `conda activate dapt619` in it first.
3. Create a new file called `addition.py` (`touch addition.py`, then open it in VS Code) and write the following code into it:

   ```python
   def add_number(a, b):
       return a + b


   print(add_number(3, 5))
   ```

4. Run the script with `python addition.py`. It prints `8`.
5. Add a test to the same file:

   ```python
   def test_add_number():
       assert add_number(3, 5) == 8
   ```

6. Run `pytest -q addition.py`. It reports `1 passed`.
   - Pytest collects functions whose names start with `test_`. If you run `pytest` with no file name, it collects only files named `test_*.py` or `*_test.py`, so `addition.py` is found only when you name it explicitly.
7. Add a few more checks:

   ```python
   def test_add_number():
       assert add_number(3, 5) == 8
       assert add_number(-1, 1) == 0
       assert add_number(0, 0) == 0
   ```

8. Run again. It still reports `1 passed`: one test function, three asserts.
9. Introduce a typo: change `return a + b` to `return a - b`. Three asserts: how many will fail? Run `pytest -q addition.py`. Pytest reports **`1 failed`**, showing only `assert -2 == 8`.
   - A test stops at its **first** failing assert, so the other two never ran.
   - `add_number(0, 0)` would have passed even with the typo. A test case where `a + b` and `a - b` agree catches nothing.
   - This is the reason for `@pytest.mark.parametrize` (Demo 2): each case becomes its own test, and one failure no longer hides the others.
10. Fix the typo (back to `a + b`) and re-run. All green again.
11. Start Python in the same folder (`python`), import the function (`from addition import add_number`; it prints `8`, because importing a file runs it), and try `add_number('a', 'b')`. It does **not** crash: Python returns `'ab'`. Then try `add_number('a', 5)`, which raises `TypeError: can only concatenate str (not "int") to str`. Neither is what we want from a function called `add_number`. Python has no idea we meant numbers. This is the Mars Climate Orbiter problem: wrong input, no crash, plausible-looking output. Leave Python with `exit()`.
12. Make the function reject anything that is not a number, with a clear error:

    ```python
    def add_number(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("add_number expects two numbers")
        return a + b
    ```

13. Test the new behavior. Add `import pytest` at the **top** of `addition.py`, then this test. `pytest.raises` passes only if the code inside it raises that error:

    ```python
    def test_add_number_rejects_strings():
        with pytest.raises(TypeError):
            add_number('a', 'b')
    ```

14. Run `pytest -q addition.py` again: `2 passed`. The **old** test still passes: we changed the function, and the old test confirms we didn't break anything.

## Demo 2: `percent_change` (files: `src/metrics.py`, `src/test_metrics.py`; tutorial version: `src/test_metrics_tutorial.py`)

1. Start from the spec, not the code. Agree on expected outputs before writing anything:

   | old | new | expected |
   |---:|---:|---:|
   | 80 | 100 | 25.0 |
   | 100 | 80 | -20.0 |
   | 50 | 50 | 0.0 |
   | 3 | 3.3 | 10.0 |
   | -50 | -25 | 50.0 (a business decision!) |
   | 0 | 10 | error (`ValueError`) |

2. Show `src/metrics.py`:

   ```python
   def percent_change(old, new):
       """Percent change from old to new. 80 -> 100 is 25.0"""
       if old == 0:
           raise ValueError("old value cannot be zero")
       return (new - old) / abs(old) * 100
   ```

3. Turn the table into one parametrized test:

   ```python
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
   ```

   Run `pytest -v src/test_metrics.py`: four separate lines, one per case.

4. Floats: `assert percent_change(3, 3.3) == 10.0` **fails** with `assert 9.999999999999993 == 10.0`. Fix it with `pytest.approx(10.0)`. (Same reason `0.1 + 0.2 == 0.3` is `False`.)
5. Errors: test that the zero case fails the right way:

   ```python
   def test_percent_change_zero_old():
       with pytest.raises(ValueError):
           percent_change(0, 10)
   ```

6. Run `pytest -q src/test_metrics.py`: `6 passed`.

## Exercise 1 (15–20 min): test a real dataset

Files: `src/heart_tutorial.py` (fill in the blanks) or `src/heart.py` (complete; just run it). Data: `data/heart.csv` (Heart Failure Prediction, fedesoriano on Kaggle, 918 rows × 12 columns). Run everything from the repo root.

**Part A (about 10 min)**

1. Activate the course environment (`conda activate dapt619`). Check that `pandas` and `pytest` are installed (`pip list`).
2. Write a function `load_heart()` that loads `data/heart.csv` into a pandas DataFrame.
3. Write a test: the DataFrame has 12 columns. Run `pytest -v src/heart_tutorial.py`. It should pass.
4. Write a test: there are no null values in any column. It should pass.
5. Write a test: the column `heart_disease` is present. It **fails**. Read the error message and figure out why. (The column is `HeartDisease`.)

**Part B (about 5–10 min, pick two)**

6. `Age` is between 18 and 100.
7. `Sex` only contains `"M"` or `"F"`.
8. `HeartDisease` only contains 0 and 1.
9. `Cholesterol` is greater than 0. Put the number of bad rows in the assert message:

   ```python
   bad = (df["Cholesterol"] <= 0).sum()
   assert bad == 0, f"{bad} rows have Cholesterol <= 0"
   ```

**Debrief:** 172 rows (19%) have `Cholesterol = 0`, and 1 row has `RestingBP = 0`. These are missing values in disguise, and the "no nulls" test passed anyway. A failing test is often a question for whoever owns the data, not just a bug.
