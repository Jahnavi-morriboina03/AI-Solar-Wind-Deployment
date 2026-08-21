from backend.app.forecasting.forecast_service import (
    ForecastService
)


def test_solar_forecast():

    service = ForecastService()

    result = service.generate_forecast(
        "Solar",
        100,
        5.5,
        0
    )


    assert result["source"]=="solar"



def test_wind_forecast():

    service = ForecastService()

    result = service.generate_forecast(
        "Wind",
        100,
        0,
        8
    )


    assert result["source"]=="wind"



def test_hybrid_forecast():

    service = ForecastService()

    result = service.generate_forecast(
        "Hybrid",
        200,
        6,
        7
    )


    assert (
        result["source"]
        ==
        "hybrid"
    )