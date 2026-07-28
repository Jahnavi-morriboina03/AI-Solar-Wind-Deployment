from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_good_site():

    payload = {
        "solar_irradiance": 6.2,
        "wind_speed": 6.8,
        "slope": 2,
        "distance_to_grid": 3,
        "distance_to_road": 1
    }

    response = client.post("/analysis", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "solar" in data
    assert "wind" in data
    assert "evaluation" in data
    assert "deployment" in data


def test_poor_site():

    payload = {
        "solar_irradiance": 2.0,
        "wind_speed": 2.5,
        "slope": 15,
        "distance_to_grid": 40,
        "distance_to_road": 20
    }

    response = client.post("/analysis", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "evaluation" in data
    assert "deployment" in data


def test_invalid_input():

    payload = {
        "solar_irradiance": -5,
        "wind_speed": 6,
        "slope": 2,
        "distance_to_grid": 2,
        "distance_to_road": 1
    }

    response = client.post("/analysis", json=payload)

    # If your API validates the input, expect 400 or 422.
    # If it raises ValueError, update the API to return HTTPException.

    assert response.status_code in [400, 422, 500]