import requests
from src.model.forecast import Condition, DailyForecast


class OpenWeatherForecastFetcher:
    api_url: str
    api_key: str
    latitude: float
    longitude: float

    def __init__(
        self, api_url: str, api_key: str, latitude: float, longitude: float
    ) -> None:
        self.api_url = api_url
        self.api_key = api_key
        self.latitude = latitude
        self.longitude = longitude

    def get_weekly_forecast(self):
        api_response = requests.get(
            f"{self.api_url}/data/2.5/onecall",
            params={
                "lat": self.latitude,
                "lon": self.longitude,
                "exclude": "hourly,minutely,current",
                "appid": self.api_key,
                "units": "metric"
            },
        )
        forecast = api_response.json()["daily"]
        mapped_forecast = [
            DailyForecast(
                date=day["dt"],
                temperature=day["temp"]["day"],
                humidity=day["humidity"],
                condition=self._map_condition(day["weather"][0]["id"]),
            )
            for day in forecast
        ]
        return mapped_forecast[:7]

    def _map_condition(self, weather_id: int) -> Condition:
        if weather_id == 800:
            return Condition.CLEAR
        elif weather_id > 800:
            return Condition.OK
        else:
            return Condition.BAD
