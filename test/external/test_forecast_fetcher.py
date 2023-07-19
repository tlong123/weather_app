import pprint
import freezegun
import pytest

from src.external.forecast_fetcher import ForecastFetcher
from src.external.open_weather_forecast_fetcher import OpenWeatherForecastFetcher
from src.external.static_forecast_fetcher import StaticForecastFetcher


@freezegun.freeze_time("2023-07-18")
@pytest.fixture(scope="function", params=["local", "open_weather"])
def forecast_fetcher(request: pytest.FixtureRequest) -> ForecastFetcher:
    if request.param == "local":
        return StaticForecastFetcher()
    elif request.param == "open_weather":
        api_url = "http://localhost:4001"
        api_key = "fake"
        lat = 5
        lon = -4
        return OpenWeatherForecastFetcher(api_url, api_key, lat, lon)


@pytest.mark.integration
def test_forecast_fetcher_returns_weekly_forecast(forecast_fetcher):
    forecast = forecast_fetcher.get_weekly_forecast()
    assert len(forecast) == 7
    assert StaticForecastFetcher().get_weekly_forecast() == forecast
