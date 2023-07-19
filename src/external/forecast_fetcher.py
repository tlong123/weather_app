import abc

from src.model.forecast import DailyForecast


class ForecastFetcher(abc.ABC):
    @abc.abstractmethod
    def get_weekly_forecast() -> list[DailyForecast]:
        pass
