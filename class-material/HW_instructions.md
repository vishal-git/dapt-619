# Homework: Customer Churn

**Due:** Thursday, December 3, 2026, 11:59 PM (submit your GitHub repo link)
**Data:** Use `data/churn_raw.csv` in the course repo

## The tasks

Here are the tasks that you need to perform for this homework exercise:

1. Find out whether the data can be trusted.
2. Find the patterns behind churn.
3. Build and compare a few churn prediction models.
4. Create a small app that the stakeholders (the churn retention team) can use.

Most of the points go to your **judgment calls** (what counts as a data problem and what to do about it, and which model to trust) and to evidence that you actually ran the code.

## Setup (Part 0)

1. Create a **new public repo** named `dapt619-churn-<your-last-name>` on GitHub.
2. In Git Bash, go to the folder that contains your `dapt-619` clone, update it, and clone your new repo next to it:

   ```bash
   cd dapt-619 && git pull && cd ..
   git clone https://github.com/<your-username>/dapt619-churn-<your-last-name>.git
   cd dapt619-churn-<your-last-name>
   ```

3. Copy the starter files and the data into your repo:

   ```bash
   cp -r ../dapt-619/homework/. .                   # starter files, including the hidden .gitignore
   cp ../dapt-619/data/churn_raw.csv data/raw/      # the raw data
   ls -a; ls src tests data/raw                     # check what's there
   ```

   You now have this layout:

   ```
   dapt619-churn-<last-name>/
   ├── README.md            # your report: fill in each section
   ├── README.docx          # the same report as a Word file, if you prefer Word
   ├── pyproject.toml       # tells pytest that your code lives in src/
   ├── .gitignore
   ├── data/raw/churn_raw.csv
   ├── notebooks/           # optional: exploration
   ├── src/                 # cleaning.py, explore.py, train.py, app.py
   ├── tests/               # test_raw_data.py, test_cleaning.py
   ├── models/              # your saved model goes here
   └── screenshots/         # the app screenshots for your README
   ```

4. Create an environment for the project and install the packages:

   ```bash
   conda create -n churn python=3.12 -y
   conda activate churn
   pip install polars pyarrow pandas scikit-learn pytest gradio matplotlib joblib tabicl
   pip list --format=freeze > requirements.txt
   ```

   Use `pip list --format=freeze`, not `pip freeze`. Inside a conda environment, `pip freeze` can write lines like `package @ file:///...` that won't install on anyone else's computer.

   If `tabicl` won't install (this happens on older Intel Macs), install everything else and see the Google Colab note in Part 3.

5. Commit as you go: **at least 5 commits** with messages that say what changed. (A simple "updated some code" is not a commit message!)
6. Commit the data file, the saved model, and your screenshots too. Someone who clones your repo should be able to run your tests and your app without retraining anything.

Run every command from the repo root (`dapt619-churn-<last-name>/`), for example `pytest -v` or `python src/app.py`.

## Part 1: Can we trust the data? (pytest)

1. In `tests/test_raw_data.py`, write **at least 6 tests** (the two examples in the starter file count) that state what the raw data *should* look like. (Think like the billing team: IDs, ages, charges, category labels, the target.)
2. Run `pytest -v`. Some of these tests will fail, **and that is expected**: each failure is a data problem you discovered.
3. In your README, fill in a **data issues table**, one row per problem:

   | # | Problem | Rows affected | How you found it | What did you do about it, and why |
   |---|---|---|---|---|

   There is no single right decision for every problem. Just provide a clear, defensible reason.
4. Write `clean()` in `src/cleaning.py` to apply your decisions. Do not edit the raw file.
5. In `tests/test_cleaning.py`, write **at least 3 tests** for `clean()`. Use a small, hand-made DataFrame as a fixture, so that you know the correct answer just by looking at it.
6. Paste the final `pytest -v` output into your README.

Some of your initial `test_raw_data.py` tests are **expected to fail** on the raw file. But every test in `test_cleaning.py` **must pass**.

## Part 2: What drives churn? (Polars)

In `src/explore.py`, use **Polars** on the cleaned data to answer two questions with a small table each:

1. Churn rate by contract type.
2. One question of your own that the retention team would care about.

Then rewrite one of your queries as a **lazy** query with `pl.scan_csv(...)` and paste its `.explain()` output into your README. Explain in one sentence what Polars optimized.

## Part 3: Predict churn (scikit-learn + TabICL)

1. In `src/train.py`, compare **three models** using **3-fold stratified cross-validation** with `random_state=314`:
   - logistic regression,
   - a gradient-boosted tree model (e.g., `HistGradientBoostingClassifier`),
   - `TabICLClassifier` from `tabicl`.
2. Report the mean AUC (± its standard deviation across the 3 folds) for each model in a table, along with how long each one took.
3. In one small paragraph: which model would you put in front of the retention team, and **why**? Consider more than AUC: speed, explainability, how often it needs retraining, and cost.
4. Save the model you selected to `models/`, together with its list of feature columns (the app needs both; see the starter `train.py`).

**If `tabicl` won't install on your computer:** run the TabICL part in [Google Colab](https://colab.research.google.com/). Upload `churn_raw.csv` and `src/cleaning.py` to the Colab session, run `!pip install polars tabicl` in the first cell, then run the same cross-validation for TabICL and copy its numbers into your table. Say in your README that this model ran in Colab. Your app can then use one of the other two models.

## Part 4: An app for the retention team (Gradio)

Fill in `src/app.py`: the retention team enters a customer's details and gets a churn probability from your saved model.

- Bad input (such as negative monthly charges) should show a clear error message, not crash the app. In Gradio, `raise gr.Error("...")` inside your function shows that message in the browser.
- Add **two screenshots** to the README: one prediction, and the error message.

## README sections (checklist)

Fill in either `README.md` or `README.docx` (the same template as a Word file), and commit the one you used. In the Word file, paste the screenshots directly into the document.

- [ ] How to run: clone, create the environment, `pip install -r requirements.txt`, `pytest`, `python src/app.py` (say which raw-data tests are expected to fail)
- [ ] Data issues table + final `pytest -v` output
- [ ] Polars tables + lazy `.explain()` output
- [ ] Model comparison table + model choice paragraph
- [ ] Two app screenshots

## Grading (100 points)

| Part | Points | What earns them |
|---|---:|---|
| 0 · Repo & reproducibility | 15 | Layout as above; `requirements.txt`; ≥ 5 meaningful commits; data, model, and screenshots committed; "How to run" works on a fresh clone |
| 1 · Data quality & tests | 30 | ≥ 6 raw-data tests; issues table that finds the real problems with sensible, justified decisions; ≥ 3 fixture-based tests for `clean()`, all passing (raw-data tests are expected to fail) |
| 2 · Polars | 15 | Two correct tables; lazy query with `.explain()` and a correct one-line explanation |
| 3 · Models | 25 | Correct CV setup (seed 314); results table; a model choice backed by more than AUC |
| 4 · Gradio app | 15 | Predictions work; clear error on bad input; screenshots |
