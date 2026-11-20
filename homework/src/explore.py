"""Part 2: what drives churn? Run from the repo root:  python src/explore.py"""
import polars as pl
from cleaning import clean, load_raw

df = clean(load_raw())

# step 1: churn rate by contract type (number of customers and churn rate per contract type)
# --

# step 2: your own question for the retention team (combining two columns is a good idea)
# --

# step 3: one of your queries as a lazy query: start from pl.scan_csv("data/raw/churn_raw.csv"),
#         then print(q.explain())
# --
