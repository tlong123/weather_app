from src.external.forecast_fetcher import ForecastFetcher
from src.model.forecast import Condition, DailyForecast
from datetime import datetime, timezone, timedelta


class StaticForecastFetcher(ForecastFetcher):
    def get_weekly_forecast(self) -> list[DailyForecast]:
        tzinfo = timezone(timedelta(0))

        return [
            DailyForecast(
                date=datetime(2023, 7, 18, 12, 0, tzinfo=tzinfo),
                temperature=20.18,
                humidity=65.0,
                condition=Condition.OK,
            ),
            DailyForecast(
                date=datetime(2023, 7, 19, 12, 0, tzinfo=tzinfo),
                temperature=19.39,
                humidity=65.0,
                condition=Condition.OK,
            ),
            DailyForecast(
                date=datetime(2023, 7, 20, 12, 0, tzinfo=tzinfo),
                temperature=17.33,
                humidity=64.0,
                condition=Condition.BAD,
            ),
            DailyForecast(
                date=datetime(2023, 7, 21, 12, 0, tzinfo=tzinfo),
                temperature=18.12,
                humidity=55.0,
                condition=Condition.OK,
            ),
            DailyForecast(
                date=datetime(2023, 7, 22, 12, 0, tzinfo=tzinfo),
                temperature=17.11,
                humidity=73.0,
                condition=Condition.BAD,
            ),
            DailyForecast(
                date=datetime(2023, 7, 23, 12, 0, tzinfo=tzinfo),
                temperature=17.81,
                humidity=83.0,
                condition=Condition.BAD,
            ),
            DailyForecast(
                date=datetime(2023, 7, 24, 12, 0, tzinfo=tzinfo),
                temperature=17.55,
                humidity=82.0,
                condition=Condition.BAD,
            ),
        ]
