# model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Sample data (replace with real dataset if available)
data = {
    'temperature': [30, 25, 28, 22, 35, 20],
    'humidity': [70, 80, 75, 90, 65, 85],
    'pressure': [1012, 1010, 1011, 1008, 1015, 1009],
    'wind_speed': [5, 3, 6, 2, 7, 4],
    'rainfall_percentage': [60, 80, 70, 90, 50, 85]
}

df = pd.DataFrame(data)

# Features and target
X = df[['temperature', 'humidity', 'pressure', 'wind_speed']]
y = df['rainfall_percentage']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'model.joblib')

print("Model trained and saved as model.joblib")
