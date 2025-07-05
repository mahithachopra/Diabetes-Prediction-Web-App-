# train_model.py
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
from data_preprocessing import load_and_preprocess

(X_train, X_test, y_train, y_test), scaler = load_and_preprocess()

model = LogisticRegression()
model.fit(X_train, y_train)
preds = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, preds))

joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')
