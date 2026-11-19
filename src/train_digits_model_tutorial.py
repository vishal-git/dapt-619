from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

digits = load_digits()
X, y = digits.data, digits.target

# step 1: split into train and test sets (random_state=314, stratify=y)
# --

# step 2: create an SVC with gamma=0.001 and C=10, and fit it
# --

# step 3: print the test accuracy
# --

# step 4: save the model to ./models/digit_model.pkl with joblib
# --
