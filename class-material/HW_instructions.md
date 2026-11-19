# Homework: Customer Churn, End to End

**Due:** Thursday, December 3, 2026, 11:59 PM (submit your GitHub repo link)
**Expected effort:** 2–3 hours
**Data:** `data/churn_raw.csv` in the course repo (3,020 rows, 15 columns)

## The scenario

You just joined the analytics team at a regional telecom company. The customer retention team wants to know **which customers are likely to cancel, and why**, so they can call them before they leave.

A colleague exported `churn_raw.csv` from the billing system before going on leave. Nobody has checked it. Your job:

1. Find out whether the data can be trusted.
2. Find the patterns behind churn.
3. Build and compare a few models.
4. Give the retention team a small app they can use.
5. Recommend what the company should do.

Most of the points go to your **judgment calls** (what counts as a data problem and what to do about it, which model to trust, what to recommend) and to evidence that you actually ran the code.

## Setup (Part 0)

1. Create a **new public GitHub repo** named `dapt619-churn-<your-last-name>`.
2. Clone it, create a conda environment for it (for example `conda create -n churn python=3.12 -y`, then `conda activate churn`), and install what you need (`polars`, `pyarrow`, `pandas`, `scikit-learn`, `pytest`, `gradio`, `matplotlib`, `tabicl`, …).
3. Lay out the project like this (the starter files in the course repo's `homework/` folder give you a head start):

   ```
   dapt619-churn-<last-name>/
   ├── README.md            # your report: see "README sections" below
   ├── requirements.txt     # pip freeze > requirements.txt
   ├── pyproject.toml       # [tool.pytest.ini_options] pythonpath = ["src"]
   ├── .gitignore           # at least __pycache__/ and .pytest_cache/
   ├── data/raw/churn_raw.csv
   ├── notebooks/           # optional: exploration
   ├── src/                 # cleaning.py, explore.py, train.py, app.py (names are up to you)
   ├── tests/               # test_raw_data.py, test_cleaning.py
   ├── models/              # your saved model: commit it (it's small)
   └── screenshots/         # the two app screenshots for your README
   ```

4. Commit as you go: **at least 5 commits** with messages that say what changed. "update" is not a commit message.
5. Commit the data file, your saved model, and your screenshots too. Someone who clones your repo should be able to run your tests and your app without retraining anything.

## Part 1: Can we trust the data? (pytest)

1. In `tests/test_raw_data.py`, write **at least 6 tests** that state what the raw data *should* look like. Think like the billing team: IDs, ages, charges, category labels, the target.
2. Run `pytest -v`. Some of these tests will fail, **and that is expected**: each failure is a data problem you found.
3. In your README, fill in a **data issues table**, one row per problem:

   | # | Problem | Rows affected | How you found it | What you did about it, and why |
   |---|---|---|---|---|

   There is no single right decision for every problem. A clear, defensible reason earns the points.
4. Write `clean()` in `src/cleaning.py` to apply your decisions. Do not edit the raw file.
5. In `tests/test_cleaning.py`, write **at least 4 tests** for `clean()`. Use a small, hand-made DataFrame as a fixture, so that you know the correct answer just by looking at it.
6. Paste the final `pytest -v` output into your README.

**To be clear about which tests should pass:** your `test_raw_data.py` tests are **expected to fail** on the raw file, one failure per problem in your issues table. Every test in `test_cleaning.py` **must pass**.

## Part 2: What drives churn? (Polars)

Using **Polars** on the cleaned data, answer three questions with a small table each:

1. Churn rate by contract type.
2. Churn rate by tenure band (you choose the bands).
3. One question of your own that the retention team would care about. Combining two columns is a good idea.

Then rewrite one of your queries as a **lazy** query with `pl.scan_csv(...)` and paste its `.explain()` output into your README. Running this one on the **raw** CSV is fine; the point is the query plan, not the numbers. Explain in one sentence what Polars optimized.

## Part 3: Which model? (scikit-learn + TabICL)

1. Compare **three models** using **5-fold stratified cross-validated AUC** with `random_state=314`:
   - logistic regression,
   - a gradient-boosted tree model (e.g., `HistGradientBoostingClassifier`),
   - `TabICLClassifier` from `tabicl`.
2. Report the mean ± standard deviation of the AUC for each model in a table, along with how long each one took.
3. In one paragraph: which model would you put in front of the retention team, and **why**? Consider more than AUC: speed, explainability, how often it needs retraining, and cost.
4. Save the model you picked to `models/`.

## Part 4: An app for the retention team (Gradio)

Build `src/app.py` with `gr.Blocks` and two tabs:

1. **Explore:** pick a column from a dropdown and see a chart of churn rate by that column.
2. **Predict:** enter a customer's details and get a churn probability from your saved model. Bad input (such as negative charges) should give a clear error message, not a crash.

Add **two screenshots** of your running app to the README, one per tab.

## Part 5: Your recommendation

**What would your recommendation be to the stakeholders?**

Answer in your README in plain English (no code, about half a page). Back it up with numbers from Parts 2 and 3, and say which customers the retention team should focus on first. Also say what you would **not** trust yet about this analysis.

## README sections (checklist)

- [ ] How to run: clone, create the environment, `pip install -r requirements.txt`, `pytest`, `python src/app.py` (say which raw-data tests are expected to fail)
- [ ] Data issues table + final `pytest -v` output
- [ ] Polars tables + lazy `.explain()` output
- [ ] Model comparison table + model choice paragraph
- [ ] Two app screenshots
- [ ] Your recommendation to the stakeholders

## Grading (100 points)

| Part | Points | What earns them |
|---|---:|---|
| 0 · Repo & reproducibility | 10 | Structure as above; `requirements.txt`; `.gitignore`; ≥ 5 meaningful commits; data, model, and screenshots committed; "How to run" works on a fresh clone |
| 1 · Data quality & tests | 25 | ≥ 6 raw-data tests; issues table that finds the real problems with sensible, justified decisions; ≥ 4 fixture-based tests for `clean()`, all passing (raw-data tests are expected to fail) |
| 2 · Polars | 10 | Three correct tables; lazy query with `.explain()` and a correct one-line explanation |
| 3 · Models | 20 | Correct CV setup (seed 314); results table; a model choice backed by more than AUC |
| 4 · Gradio app | 15 | Both tabs work; graceful error on bad input; screenshots |
| 5 · Recommendation | 20 | A clear, actionable recommendation backed by numbers; honest limitations |
