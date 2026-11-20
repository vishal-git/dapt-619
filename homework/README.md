# Customer churn: <your name>

DAPT 619 · Fall 2026 homework. Instructions: `class-material/HW_instructions.md` in the course repo.

## How to run

```bash
git clone <your repo url>
cd <repo>
conda create -n churn python=3.12
conda activate churn
pip install -r requirements.txt
pytest -v
python src/app.py
```

Expected: the tests in `tests/test_raw_data.py` that check for the problems below **fail** on the raw file (one per issue); every test in `tests/test_cleaning.py` passes.

## 1. Data issues

| # | Problem | Rows affected | How you found it | What you did about it, and why |
|---|---|---|---|---|
| 1 | | | | |

Final `pytest -v` output:

```
paste here
```

## 2. What drives churn?

### Churn rate by contract type

### My question:

### Lazy query plan

```
paste .explain() output here
```

What Polars optimized:

## 3. Model comparison

| Model | CV AUC (mean ± sd) | Time |
|---|---|---|
| Logistic regression | | |
| Gradient boosting | | |
| TabICL | | |

Which model I would deploy, and why:

## 4. App

![A prediction](screenshots/prediction.png)
![The error message for bad input](screenshots/error.png)

## 5. Recommendation

What would your recommendation be to the stakeholders?
