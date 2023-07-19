from typing import Annotated
from fastapi import FastAPI, Depends
from os import environ
from src.external.open_weather_forecast_fetcher import OpenWeatherForecastFetcher

from src.service.commute_planner import CommutePlanner
from src.external.static_forecast_fetcher import StaticForecastFetcher

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

env = environ.get("environment", "DEVELOPMENT")

forecast_fetcher: CommutePlanner

if env != "DEVELOPMENT":
    forecast_fetcher =lambda: CommutePlanner(OpenWeatherForecastFetcher(
        "https://api.openweathermap.org",
        environ["OPEN_WEATHER_API_KEY"],
        50.8244439,
        -0.1416104,
    ))
else:
    forecast_fetcher = lambda: CommutePlanner(StaticForecastFetcher())

Planner = Annotated[CommutePlanner, Depends(forecast_fetcher)]


@app.get("/weather/today")
def get_current_weather(planner: Planner):
    return planner.weather_for_today()


@app.get("/weather/best")
def get_best_weather(planner: Planner):
    return planner.best_weather()
