from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Your OpenWeatherMap API key
API_KEY = "a700d996f1e78816f02097cdf268dc39"

# Endpoint to get current weather for a specific city
@app.route("/weather/<city>")
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        return jsonify({
            "temperature": weather_data["main"]["temp"],
            "condition": weather_data["weather"][0]["description"]
        })
    else:
        return jsonify({"error": "City not found"})

# Default route to make http://localhost:5000 work
@app.route("/")
def index():
    return "Welcome to the Weather API!"

if __name__ == "__main__":
    app.run(debug=True)
