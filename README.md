Weather Microservice
A lightweight microservice built with FastAPI that fetches real-time weather data for a given city using the OpenWeatherMap API. The service is containerized with Docker for easy deployment.

Features
Fetch current weather data (temperature, humidity, wind speed, etc.).
Accepts a city name as input.
Securely uses environment variables for API keys.
Setup Instructions
1. Prerequisites
Python installed
Docker Desktop installed(optional)
OpenWeatherMap API key
2. Installation
Clone the repository:


git clone <repository-url>

Create a .env file and add your API key:

makefile
Copy
Edit
OPENWEATHER_API_KEY=your_actual_api_key
Install dependencies locally (optional for testing):


pip install -r requirements.txt
3. Run Locally
To run the application locally:


uvicorn main:app --reload
Access the app at: http://localhost:8000

4. Run with Docker
Build the Docker image:


docker build -t weather-microservice .
Run the container:


docker run -d -p 8000:8000 --env-file .env weather-microservice
Access the app at: http://localhost:8000

API Endpoints
1. Home
URL: /
Method: GET
Response:

{
  "message": "Welcome to the Weather Microservice! Use /weather to fetch weather data."
}
2. Fetch Weather
URL: /weather
Method: POST
Request Body:

{
  "city": "Helsinki"
}
Response:

{
  "city": "Helsinki",
  "temperature": 2.5,
  "description": "clear sky",
  "humidity": 80,
  "wind_speed": 3.6
}