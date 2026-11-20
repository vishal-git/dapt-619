# run from the repo root:  python src/tabicl_heart.py
# The first run downloads TabICL's pretrained weights (~110 MB) from Hugging Face; later runs load them from disk.
import time

import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from tabicl import TabICLClassifier

df = pd.read_csv("data/heart.csv")
X = pd.get_dummies(df.drop(columns="HeartDisease"), drop_first=True).astype(float)  # one-hot encode the text columns
y = df["HeartDisease"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=314, stratify=y)

models = {
    "Logistic regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
    "Gradient boosting": HistGradientBoostingClassifier(random_state=314),
    "TabICL": TabICLClassifier(random_state=314),  # pretrained: fit() stores the training rows, no training happens
}

for name, model in models.items():
    start = time.perf_counter()
    model.fit(X_train, y_train)
    proba = model.predict_proba(X_test)[:, 1]
    print(f"{name:<20} test AUC = {roc_auc_score(y_test, proba):.3f}   ({time.perf_counter() - start:.1f} s)")
