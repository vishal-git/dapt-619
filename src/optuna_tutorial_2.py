import pandas as pd
from sklearn.model_selection import train_test_split
import optuna
import xgboost as xgb
from sklearn.metrics import roc_auc_score

# load the dataset
df = pd.read_csv("./data/credit_default_model_data.csv")  

# for quick demo, take a 5000-sample subset
df_sample = df.sample(n=5000, random_state=67)  

# set the target vector and features matrix 
X = df_sample.drop(columns=['default payment next month', 'group'])
y = df_sample['default payment next month']

# split into train and validation sets
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=67
)
print(f"Training samples: {len(X_train)}, Validation samples: {len(X_val)}")

# create a study object
study2 = optuna.create_study(
    study_name="credit_default_round2",
    direction="maximize",
    storage="sqlite:///optuna_credit.db",  # store results in a database file
    load_if_exists=True
)

def objective(trial):
    # suggest hyperparameter values for this trial:
    params = {
        "max_depth": trial.suggest_int("max_depth", 3, 6),
        "min_child_weight": trial.suggest_float("min_child_weight", 0.01, 0.03, step=0.01),
        "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.05, step=0.01),
        "subsample": trial.suggest_float("subsample", 0.5, 1.0, step=0.1),
        "objective": "binary:logistic",
        "eval_metric": "auc",
        "n_estimators": 100,
    }
    # train the model
    model = xgb.XGBClassifier(**params)
    model.fit(X_train, y_train, verbose=False)
    # compute validation AUC for this trial
    y_pred = model.predict_proba(X_val)[:, 1]
    auc = roc_auc_score(y_val, y_pred)
    return auc

# run the optimization for a limited number of trials (for a demo)
study2.optimize(objective, n_trials=30)
