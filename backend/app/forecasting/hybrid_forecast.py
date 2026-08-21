from .solar_forecast import forecast_solar_energy
from .wind_forecast import forecast_wind_energy



def forecast_hybrid_energy(
        total_capacity_kw,
        solar_irradiance,
        wind_speed
):


    solar_capacity = (
        total_capacity_kw / 2
    )

    wind_capacity = (
        total_capacity_kw / 2
    )


    solar = forecast_solar_energy(
        solar_capacity,
        solar_irradiance
    )


    wind = forecast_wind_energy(
        wind_capacity,
        wind_speed
    )


    total_energy = (
        solar["annual_energy_kwh"]
        +
        wind["annual_energy_kwh"]
    )


    return {

        "source":"hybrid",

        "solar":
            solar,

        "wind":
            wind,

        "total_annual_energy_kwh":
            round(total_energy,2)

    }