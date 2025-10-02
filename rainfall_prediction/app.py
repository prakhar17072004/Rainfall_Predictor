from flask import Flask, render_template, request
import joblib
import numpy as np
import requests

app = Flask(__name__)

# Load trained ML model
model = joblib.load('model.joblib')

# OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"  # Replace with your key

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    weather_data = {}
    
    if request.method == 'POST':
        # Get lat & lon from form
        lat = request.form['lat']
        lon = request.form['lon']
        
        # Call OpenWeatherMap API
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        
        weather_data = {
            'temperature': temperature,
            'humidity': humidity,
            'pressure': pressure,
            'wind_speed': wind_speed
        }

        # Predict rainfall
        input_features = np.array([[temperature, humidity, pressure, wind_speed]])
        prediction = model.predict(input_features)[0]
        prediction = round(prediction, 2)
    
    return render_template('index.html', prediction=prediction, weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
