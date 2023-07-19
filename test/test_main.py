from freezegun import freeze_time
from src.main import app
from fastapi.testclient import TestClient
from datetime import datetime, timedelta

from src.model.forecast import Condition


@freeze_time("2023-07-18T012:00:00")
def test_get_todays_weather_returns_todays_weather_forecast():
    client = TestClient(app)
    response = client.get("/weather/today")
    assert response.status_code == 200
    assert response.json() == {
        "date": datetime.today().isoformat() + "Z",
        "condition": Condition.OK,
        "temperature": 20.18,
        "humidity": 65,
    }


@freeze_time("2023-07-13T012:00:00")
def test_get_best_weather_returns_best_days_weather_for_the_week():
    client = TestClient(app)
    response = client.get("/weather/best")
    assert response.status_code == 200
    assert response.json() == {
        "date": (datetime.today() + timedelta(days=5)).isoformat() + "Z",
        "condition": str(Condition.OK),
        "temperature": 20.18,
        "humidity": 65,
    }
