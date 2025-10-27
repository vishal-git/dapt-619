from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

digits = load_digits()
X, y = digits.data, digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=314, stratify=y)

clf = SVC(gamma=0.001, C=10)  # classic setting for this dataset
clf.fit(X_train, y_train)
print(f"Test accuracy: {accuracy_score(y_test, clf.predict(X_test)):.2%}")

joblib.dump(clf, "./models/digit_model.pkl")
