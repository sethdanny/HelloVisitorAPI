#!/usr/bin/python3
"""Start the flask application"""


from flask import Flask, request, jsonify
from dotenv import load_dotenv
from os import getenv
import requests


load_dotenv()

app = Flask(__name__)

IP_INFO_TOKEN = getenv('IP_INFO_TOKEN')
OPENWEATHERMAP_API_KEY = getenv('OPENWEATHERMAP_API_KEY')


@app.route('/api/hello', methods=['GET'], strict_slashes=False)
def index():
    """
    Endpoint to greet the visitor and provide weather
    information based on their IP address.

    This endpoint takes a query parameter 'visitor_name' and
    uses the requester's IP address to determine their location.
    It then fetches the current temperature for that location
    and returns a greeting message along with the temperature.

    Query Parameters:
    - visitor_name (str): The name of the visitor to greet.

    Returns:
    - JSON response with the following structure:
        {
            "client_ip": "127.0.0.1",  # The IP address of the requester
            "location": "New York",  # The city of the requester
            "greeting": "Hello, Mark!, the temperature is 11 degrees
            Celsius in New York"  # A greeting message with the temperature
        }
    """
    visitor_name = request.args.get('visitor_name', 'Mark')
    client_ip = request.remote_addr

    ipinfo_url = 'https://ipinfo.io/{}?token={}'.format(
        client_ip, IP_INFO_TOKEN)

    location_response = requests.get(ipinfo_url)
    """if location_response.status_code != 200:
        return jsonify({
            "error": "Failed to fetch location information"
        }), 500 """
    location_data = location_response.json()
    #print(f"IP Info Response Status Code: {location_response.status_code}")  # Print status code
    print(f"IP Info Response Data:\n{location_data}")  # Print entire response for inspection
    location = location_data.get('city', 'unknown')

    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'.format(
        location, OPENWEATHERMAP_API_KEY)
    weather_response = requests.get(weather_url)
    """if weather_response.status_code != 200:
        return jsonify({
            "error": "Failed to fetch weather information"
        }), 500 """
    weather_data = weather_response.json()
    print(f"OpenWeatherMap Response Status Code: {weather_response.status_code}")  # Print status code
    print(f"OpenWeatherMap Response Data:\n{weather_data}")  # Print entire response for inspection
    temperature = weather_data.get('main', {}).get(
        'temp', 'unknown temperature')

    response = {
        "client_ip": client_ip,
        "location": location,
        "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
