# 🧠 Diabetes Prediction Web App

This is a **Data Science project** that predicts whether a person is diabetic or not based on health metrics. It uses a **machine learning model**, exposed via a **FastAPI backend**, and a **Streamlit frontend** for user interaction.

---

## 📌 Project Overview

This project demonstrates an end-to-end deployment of a machine learning model using:

- **Data preprocessing** with `pandas` and `scikit-learn`
- **Model training** and serialization with `joblib`
- **API backend** using FastAPI to serve predictions
- **Frontend** using Streamlit to interact with the model
- **Dataset**: [Pima Indian Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

---

## 🚀 Features

- Clean and preprocess dataset
- Train and evaluate a predictive ML model
- Expose prediction API via FastAPI
- Simple and responsive UI with Streamlit
- Real-time prediction from user input

---

## 🗂️ Project Structure

diabetes-prediction-app/
│
├── app.py # FastAPI backend
├── data_preprocessing.py # Preprocessing logic
├── main.py # Streamlit frontend
├── model.pkl # Trained ML model
├── diabetes.csv # Dataset
├── requirements.txt # Project dependencies
└── README.md # Project documentation


---

## 🧪 Dataset Info

The dataset contains medical information like:

- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age

The target variable is `Outcome` (1 = Diabetic, 0 = Non-Diabetic).

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
git clone https://github.com/mahithachopra/diabetes-prediction-app.git
cd diabetes-prediction-app
### 2️⃣ Create and activate virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
### 3️⃣ Install dependencies
pip install -r requirements.txt

## ▶️ How to Run the App
### Step 1: Start FastAPI backend
uvicorn app:app --reload
This will launch the API at http://127.0.0.1:8000.

You can test it by sending a POST request to:
arduino
http://127.0.0.1:8000/predict
### Step 2: Launch the Streamlit frontend
In a new terminal window:
streamlit run main.py
The app UI will open in your default browser.

## 📊 Sample Prediction Flow
Enter patient health parameters in the Streamlit form.
Click Predict.
The app sends a request to the FastAPI server.
Server responds with a prediction (Diabetic or Non-Diabetic).
![Screenshot 2025-07-05 114940](https://github.com/user-attachments/assets/a6917d2f-1a4d-4fb8-8ce7-7f2f846052fc)
![Screenshot 2025-07-05 114955](https://github.com/user-attachments/assets/754cade7-0cb9-4dff-a123-1f52de14ddda)


## 📈 Model Training (Optional)
To retrain or update the model:
Run data_preprocessing.py to get the processed dataset and scaler
Train a classifier (e.g., LogisticRegression) and save it as model.pkl using joblib
Save the scaler as scaler.pkl as well


## 🙋‍♀️ Author
Mahitha Chopra Lankapalli
MSc AI & Data Science
Central University of Andhra Pradesh

✨ Feel free to fork this repo, give it a ⭐, and contribute!











Ask ChatGPT
