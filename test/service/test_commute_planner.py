from datetime import datetime, timedelta

import freezegun

from src.model.forecast import Condition, DailyForecast
from src.service.commute_planner import CommutePlanner


def forecast_with_data(week_data: list[tuple[float, float]]) -> list[DailyForecast]:
    today = datetime.today()
    forecast = []
    for i, data in enumerate(week_data):
        forecast.append(
            DailyForecast(
                date=today + timedelta(days=i),
                temperature=data[0],
                humidity=data[1],
                condition=Condition.OK,
            )
        )
    return forecast


def forecaster_with_data(data: list[tuple[float, float]]):
    class StubForecaster:
        def get_weekly_forecast(self):
            return forecast_with_data(data)

    return StubForecaster()


@freezegun.freeze_time("2023-07-15")
def test_returns_todays_weather_from_forecast():
    stub_forecaster = forecaster_with_data([(21, 50)] * 7)
    planner = CommutePlanner(stub_forecaster)

    assert planner.weather_for_today() == stub_forecaster.get_weekly_forecast()[0]


@freezegun.freeze_time("2023-07-15")
def test_gets_best_day_with_highest_temp():
    stub_forecaster = forecaster_with_data([(21, 50)] * 6 + [(22, 50)])
    planner = CommutePlanner(stub_forecaster)

    assert planner.best_weather() == stub_forecaster.get_weekly_forecast()[6]


@freezegun.freeze_time("2023-07-15")
def test_gets_best_day_with_highest_temp_and_lowest_humidity_if_two_days_with_same_temp():
    stub_forecaster = forecaster_with_data([(21, 50)] * 5 + [(22, 50)] + [(22, 49)])
    planner = CommutePlanner(stub_forecaster)

    assert planner.best_weather() == stub_forecaster.get_weekly_forecast()[6]


@freezegun.freeze_time("2023-07-15")
def test_gets_best_working_day_if_best_day_is_on_the_weekend():
    stub_forecaster = forecaster_with_data([(25, 50)] + [(21, 50)] * 5 + [(22, 50)])
    planner = CommutePlanner(stub_forecaster)

    assert planner.best_weather() == stub_forecaster.get_weekly_forecast()[6]


@freezegun.freeze_time("2023-07-15")
def test_chooses_soonest_day_if_matching_temp_and_humidity():
    stub_forecaster = forecaster_with_data([(25, 50)] + [(21, 50)] * 4 + [(22, 50)] * 2)
    planner = CommutePlanner(stub_forecaster)

    assert planner.best_weather() == stub_forecaster.get_weekly_forecast()[5]
