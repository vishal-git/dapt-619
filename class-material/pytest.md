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
11. Try inputs that aren't numbers. At the bottom of `addition.py`, temporarily add:

    ```python
    print(add_number('x', 'y'))
    print(add_number('x', 5))
    ```

    Run `python addition.py`. It prints `8`, then `xy`: adding two strings does **not** crash, it glues them together. Then the second line raises `TypeError: can only concatenate str (not "int") to str`. Neither is what we want from a function called `add_number`. Python has no idea we meant numbers. This is the Mars Climate Orbiter problem: wrong input, no crash, plausible-looking output.

    Delete the two lines when you're done.
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
            add_number('x', 'y')
    ```

14. Run `pytest -q addition.py` again: `2 passed`. The **old** test still passes: we changed the function, and the old test confirms we didn't break anything.

## Demo 2: `percent_change` (complete versions: `src/metrics.py`, `src/test_metrics.py`)

1. Copy the function and the tutorial test file into your `pytest-demo` folder (from inside `pytest-demo`):

   ```bash
   cp ../dapt-619/src/metrics.py ../dapt-619/src/test_metrics_tutorial.py .
   ```

2. Start from the spec, not the code: agree on the expected outputs before writing anything.

   | old | new | expected |
   |---:|---:|---:|
   | 80 | 100 | 25.0 |
   | 100 | 80 | -20.0 |
   | 50 | 50 | 0.0 |
   | 3 | 3.3 | 10.0 |
   | -50 | -25 | 50.0 (a business decision!) |
   | 0 | 10 | error (`ValueError`) |

3. The function, in `metrics.py`:

   ```python
   def percent_change(old, new):
       """Percent change from old to new. 80 -> 100 is 25.0"""
       if old == 0:
           raise ValueError("old value cannot be zero")
       return (new - old) / abs(old) * 100
   ```

4. In `test_metrics_tutorial.py`, step 1: turn the table into one parametrized test. `@pytest.mark.parametrize` is a **decorator**: an `@...` line right above a `def` that changes how the function is used. Here it tells pytest to run the test once per row.

   ```python
   @pytest.mark.parametrize("old, new, expected", [
       (80, 100, 25.0),
       (100, 80, -20.0),
       (50, 50, 0.0),
       (-50, -25, 50.0),
   ])
   def test_percent_change(old, new, expected):
       assert percent_change(old, new) == expected
   ```

   Run `pytest -v test_metrics_tutorial.py`: four separate lines, one per case.

5. Step 2, floats. This test **fails**:

   ```python
   def test_percent_change_float():
       assert percent_change(3, 3.3) == 10.0
   ```

   pytest shows `assert 9.999999999999993 == 10.0`. Computers store floats in binary, and 3.3 has no exact binary form, so the result is off by a tiny amount (the same reason `0.1 + 0.2 == 0.3` is `False`). Compare with `pytest.approx` instead:

   ```python
   def test_percent_change_float():
       assert percent_change(3, 3.3) == pytest.approx(10.0)
   ```

6. Step 3, errors: test that the zero case fails the right way.

   ```python
   def test_percent_change_zero_old():
       with pytest.raises(ValueError):
           percent_change(0, 10)
   ```

7. Run `pytest -q test_metrics_tutorial.py`: `6 passed`.

## Demo 2b: testing data code with a fixture (complete versions: `src/cleaning.py`, `src/test_cleaning.py`)

1. The function under test cleans a customer table: it drops duplicate customers and tidies the state codes.

   ```python
   def clean_customers(df):
       out = df.drop_duplicates(subset="customer_id").copy()
       out["state"] = out["state"].str.strip().str.upper()
       return out
   ```

   - `.str` appears twice because `.str.strip()` returns a regular Series; the next string method needs the `.str` accessor again.
   - `.copy()` doesn't protect the input (`drop_duplicates` already returns a new DataFrame); it avoids a `SettingWithCopyWarning` in pandas 2.

2. A **fixture** is a function that builds test data. Mark it with the `@pytest.fixture` decorator; any test that names it as an argument gets a fresh copy.

   ```python
   @pytest.fixture
   def raw():
       return pd.DataFrame({"customer_id": [1, 1, 2],
                            "state": [" va", " va", "NC "]})
   ```

3. Three tests use it. The third checks something the function should **not** do: change its input. It doesn't need the function's return value, so it doesn't store it.

   ```python
   def test_removes_duplicates(raw):
       assert clean_customers(raw)["customer_id"].is_unique

   def test_normalizes_state(raw):
       assert list(clean_customers(raw)["state"]) == ["VA", "NC"]

   def test_does_not_modify_input(raw):
       before = raw.copy()
       clean_customers(raw)
       pd.testing.assert_frame_equal(raw, before)
   ```

4. Will these three tests pass or fail? Run `pytest -v src/test_cleaning.py` from the repo root: `3 passed`.

## Exercise 1 (15–20 min): test a real dataset

Files: `src/heart_tutorial.py` (fill in the blanks) and `src/heart.py` (complete version). Data: `data/heart.csv` (Heart Failure Prediction, fedesoriano on Kaggle, 918 rows × 12 columns).

**Setup.** Work on copies in your `pytest-demo` folder, so the course repo stays untouched. From inside `pytest-demo`:

```bash
mkdir data
cp ../dapt-619/data/heart.csv data/
cp ../dapt-619/src/heart_tutorial.py .
```

Run the tests with `pytest -v heart_tutorial.py`. The step numbers below match the comments in `heart_tutorial.py`.

**Part A: does the file look the way we expect? (about 10 min)**

1. Finish `load_heart()` so it returns `data/heart.csv` as a pandas DataFrame.
2. Test: the DataFrame has 12 columns. It passes.
3. Test: there are no null values in any column. It passes.
4. Test: the column `heart_disease` is present. It **fails**. Read the error message to find out why.

**Part B: does the data make sense? (about 5–10 min, pick two)**

5. `Age` is between 18 and 100.
6. `Sex` only contains `"M"` or `"F"`.
7. `HeartDisease` only contains 0 and 1.
8. `Cholesterol` and `RestingBP` are greater than 0. Put the number of bad rows in the assert message:

   ```python
   bad = (df["Cholesterol"] <= 0).sum()
   assert bad == 0, f"{bad} rows have Cholesterol <= 0"
   ```

**Stretch:** rewrite step 8 as one test with `@pytest.mark.parametrize("col", ["Cholesterol", "RestingBP"])`, so each column is its own test.

**Complete version.** From the repo root: `pytest -v src/heart.py` → `5 failed, 5 passed`. All five failures are expected:

- `test_has_heart_disease_column`: the column is called `HeartDisease`, not `heart_disease`. The test was right to fail; the assumption was wrong.
- `test_cholesterol_positive`: 172 rows have `Cholesterol <= 0`.
- `test_resting_bp_positive`: 1 row has `RestingBP <= 0`.
- `test_measurement_positive[Cholesterol]` and `[RestingBP]`: the same two checks, from the parametrized stretch version.

**Debrief.** 172 rows (19%) have `Cholesterol = 0`, and 1 row has `RestingBP = 0`. Nobody has zero cholesterol: these are missing values in disguise, and the "no nulls" test passed anyway. A failing test is often a question for whoever owns the data, not just a bug.
