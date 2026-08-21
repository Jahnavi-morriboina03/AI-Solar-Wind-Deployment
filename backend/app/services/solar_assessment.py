
from backend.app.data_sources.nasa_power import NasaPowerClient


class SolarAssessmentService:

    def __init__(self):
        self.client = NasaPowerClient()

    def get_solar_data(
        self,
        latitude: float,
        longitude: float
    ):
        return self.client.fetch(latitude, longitude)

    def classify_solar_site(
        self,
        solar_irradiance: float
    ) -> str:

        if solar_irradiance < 0:
            raise ValueError(
                "Solar irradiance cannot be negative."
            )

        if solar_irradiance < 3:
            return "Poor"

        elif solar_irradiance <= 5:
            return "Moderate"

        elif solar_irradiance <= 7:
            return "Good"

        else:
            return "Excellent"