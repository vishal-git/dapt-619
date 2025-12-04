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

# step 1: create a study object
# --

# step 2: define the objective function
# --

# step 3: run the optimization for a limited number of trials (for a demo)
# --