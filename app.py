from flask import Flask, render_template, request
import joblib
import numpy as np
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
model = joblib.load('model.joblib')
API_KEY = os.getenv('OPENWEATHER_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    prediction = None
    weather_data = {}
    location_info = {}

    city = "New Delhi"  # default city
    country = "India"

    if request.method == 'POST':
        city = request.form['city']
        country = request.form['country']

    # Call OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        country_code = data['sys']['country']
        location_name = data['name']

        weather_data = {
            'temperature': temperature,
            'humidity': humidity,
            'pressure': pressure,
            'wind_speed': wind_speed
        }

        location_info = {
            'city': location_name,
            'country': country_code
        }

        # Predict rainfall
        input_features = np.array([[temperature, humidity, pressure, wind_speed]])
        prediction = model.predict(input_features)[0]
        prediction = round(prediction, 2)
    else:
        weather_data = None
        prediction = None
        location_info = None

    return render_template('dashboard.html', weather=weather_data, prediction=prediction, location=location_info)

if __name__ == '__main__':
    app.run(debug=True)
