

class SolarAssessmentService:

    def classify_solar_site(self, solar_irradiance: float) -> str:
        """
        Classify solar energy potential.

        < 3 kWh/m²/day -> Poor
        3–5             -> Moderate
        5–7             -> Good
        > 7             -> Excellent
        """

        if solar_irradiance < 0:
            raise ValueError("Solar irradiance cannot be negative.")

        if solar_irradiance < 3:
            return "Poor"

        elif solar_irradiance <= 5:
            return "Moderate"

        elif solar_irradiance <= 7:
            return "Good"

        else:
            return "Excellent"