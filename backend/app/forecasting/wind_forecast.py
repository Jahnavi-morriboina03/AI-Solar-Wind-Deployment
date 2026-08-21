def forecast_wind_energy(
        capacity_kw: float,
        wind_speed: float
):

    """
    Estimate wind production
    """


    if wind_speed < 4:
        capacity_factor = 0.15

    elif wind_speed < 7:
        capacity_factor = 0.30

    else:
        capacity_factor = 0.45



    annual_energy = (
        capacity_kw *
        8760 *
        capacity_factor
    )


    return {
        "source":"wind",

        "annual_energy_kwh":
            round(
                annual_energy,2
            ),

        "capacity_factor":
            capacity_factor
    }