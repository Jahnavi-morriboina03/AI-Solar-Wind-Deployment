from backend.app.energy.solar_estimation import (
    estimate_annual_solar_energy
)

from backend.app.energy.wind_estimation import (
    estimate_annual_wind_energy
)


class EnergyEstimationService:

    SOLAR_CAPACITY_FACTOR = 0.20
    WIND_CAPACITY_FACTOR = 0.35

    def estimate_energy(
        self,
        site_evaluation_result: dict,
        deployment_type: str,
        installed_capacity: float
    ) -> dict:

        deployment_type = deployment_type.lower()

        solar_energy = 0.0
        wind_energy = 0.0

        if deployment_type == "solar":

            solar_energy = estimate_annual_solar_energy(
                installed_capacity=installed_capacity,
                capacity_factor=self.SOLAR_CAPACITY_FACTOR
            )

        elif deployment_type == "wind":

            wind_energy = estimate_annual_wind_energy(
                installed_capacity=installed_capacity,
                capacity_factor=self.WIND_CAPACITY_FACTOR
            )

        elif deployment_type == "hybrid":

            solar_capacity = installed_capacity / 2
            wind_capacity = installed_capacity / 2

            solar_energy = estimate_annual_solar_energy(
                installed_capacity=solar_capacity,
                capacity_factor=self.SOLAR_CAPACITY_FACTOR
            )

            wind_energy = estimate_annual_wind_energy(
                installed_capacity=wind_capacity,
                capacity_factor=self.WIND_CAPACITY_FACTOR
            )

        else:

            raise ValueError(
                "Deployment type must be Solar, Wind, or Hybrid."
            )

        total_energy = solar_energy + wind_energy

        return {
            "estimated_annual_solar_energy_mwh": solar_energy,
            "estimated_annual_wind_energy_mwh": wind_energy,
            "total_estimated_annual_energy_mwh": total_energy
        }