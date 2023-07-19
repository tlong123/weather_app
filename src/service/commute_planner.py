import pprint
from src.external.forecast_fetcher import ForecastFetcher
from src.model.forecast import DailyForecast
from datetime import datetime


class CommutePlanner:
    def __init__(self, forecast_fetcher: ForecastFetcher):
        self.forecast_fetcher = forecast_fetcher

    def weather_for_today(self) -> DailyForecast:
        weekly_forecast = self.forecast_fetcher.get_weekly_forecast()
        print(f"today is: {datetime.today()}")
        print(f"the first forecast's day is: {weekly_forecast[0].date}")
        return list(
            filter(
                lambda daily_forecast: daily_forecast.date.day == datetime.today().day,
                weekly_forecast,
            )
        )[0]

    def best_weather(self) -> DailyForecast:
        weekly_forecast: list[
            DailyForecast
        ] = self.forecast_fetcher.get_weekly_forecast()
        working_week_forecast = list(
            filter(lambda day: day.date.weekday() < 5, weekly_forecast)
        )
        working_week_forecast.sort(
            key=lambda day: (-day.temperature, day.humidity, day.date)
        )
        return working_week_forecast[0]
