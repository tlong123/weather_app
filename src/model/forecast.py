from enum import StrEnum
from pydantic import BaseModel
from datetime import datetime


class Condition(StrEnum):
    CLEAR = "Clear"
    OK = "Ok"
    BAD = "Bad"


class DailyForecast(BaseModel):
    date: datetime
    temperature: float
    humidity: float
    condition: Condition
