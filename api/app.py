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
    return 'Hello'


if __name__ == '__main__':
    app.run(host='0.0.0.', port=5000)
