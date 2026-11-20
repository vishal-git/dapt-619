"""Part 3: compare three models with 5-fold cross-validated AUC. Run from the repo root:  python src/train.py"""
import time

import joblib
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score
from tabicl import TabICLClassifier  # if tabicl won't install, see the Google Colab note in Part 3
from cleaning import clean, load_raw

SEED = 314

df = clean(load_raw())

# step 1: build the features X (a pandas DataFrame of numbers) and the target y
#         hint: drop customer_id and churn, one-hot encode the text columns with .to_dummies(),
#         then .to_pandas(); models can't use missing values, so handle any that are left
# --

# step 2: set up 5-fold stratified cross-validation with shuffle=True and random_state=SEED
# --

# step 3: for each of the three models, run cross_val_score(..., scoring="roc_auc"),
#         and print the mean and standard deviation of the AUC and how long it took
# --

# step 4: fit the model you picked on all of X and y, and save it together with its feature columns,
#         so the app can line up a new customer's columns with the ones the model was trained on:
#         joblib.dump({"model": model, "columns": list(X.columns)}, "models/churn_model.joblib")
# --
