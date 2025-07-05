# data_preprocessing.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_preprocess():
    df = pd.read_csv('diabetes.csv')
    df[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = \
        df[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0, pd.NA)
    df = df.fillna(df.median())
    
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return train_test_split(X_scaled, y, test_size=0.2, random_state=42), scaler
