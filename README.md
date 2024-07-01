# Hello Vistor API

This is a simple Flask-based API that greets visitors and provides weather information based on their IP address. The API exposes a single endpoint that accepts a visitor's name and returns a greeting along with the current temperature in the visitor's city.

## Features

- Fetches the visitor's city based on their IP address.
- Retrieves the current temperature for the visitor's city.
- Returns a personalized greeting with the temperature information.

## API Endpoint

### [GET] /api/hello

**Query Parameters:**

- `visitor_name` (optional): The name of the visitor to greet. Defaults to "Guest" if not provided.

**Response:**

```json
{
  "client_ip": "127.0.0.1",
  "location": "New York",
  "greeting": "Hello, Mark!, the temperature is 11 degrees Celsius in New York"
}
```

## Prerequisites
* Python 3.6+
* Flask
* requests library

### Setup and Installation
1. Clone the repository:
git clone https://github.com/sethdanny/HelloVisitorAPI.git
* cd HelloVisitorApi

2. Create and activate a virtual environment:
python -m venv venv
`source venv/bin/activate`  # On Windows, use `venv\Scripts\activate`

3. Install the required dependencies:
pip install -r requirements.txt

4. Set up your environment variables for the API keys. Create a .env file in the root directory and add the following:

OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
IPINFO_TOKEN=your_ipinfo_token

5. Run the Flask application:
flask run

6. Access the API endpoint:
`http://127.0.0.1:5000/api/hello?visitor_name=Mark`

## Deployment
To deploy the application to a production environment, follow these steps:

1. Push the code to your preferred hosting platform (e.g., Heroku, AWS, etc.).
2. Set the necessary environment variables for your API keys on the hosting platform.
3. Ensure the hosting platform runs the Flask application.

### License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements
* Flask
* IPinfo
* OpenWeatherMap

## Author
Nadduli Daniel <naddulidaniel94@gmail.com>


