def forecast_solar_energy(
        capacity_kw: float,
        solar_irradiance: float,
        days: int = 365
):

    """
    Estimate solar energy production
    """

    capacity_factor = solar_irradiance / 10

    if capacity_factor > 1:
        capacity_factor = 1


    annual_energy = (
        capacity_kw *
        8760 *
        capacity_factor
    )


    daily_energy = annual_energy / 365


    return {
        "source": "solar",
        "annual_energy_kwh": round(
            annual_energy,2
        ),
        "daily_energy_kwh": round(
            daily_energy,2
        ),
        "capacity_factor":
            round(capacity_factor,2)
    }