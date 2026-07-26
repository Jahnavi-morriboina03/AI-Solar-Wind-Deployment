from typing import Dict


class CapacityPlanner:
    """
    Estimates recommended renewable energy installation capacity.
    """

    def __init__(
        self,
        solar_acres_per_mw: float = 5.0,
        wind_acres_per_mw: float = 1.0,
        solar_min_score: float = 40.0,
        wind_min_score: float = 40.0
    ):
        self.solar_acres_per_mw = solar_acres_per_mw
        self.wind_acres_per_mw = wind_acres_per_mw
        self.solar_min_score = solar_min_score
        self.wind_min_score = wind_min_score

    def calculate_solar_capacity(
        self,
        land_area: float,
        solar_score: float
    ) -> float:
        """
        Calculate recommended solar capacity in MW.
        """

        if land_area <= 0 or solar_score < self.solar_min_score:
            return 0.0

        maximum_capacity = (
            land_area / self.solar_acres_per_mw
        )

        resource_factor = solar_score / 100

        capacity = maximum_capacity * resource_factor

        return round(capacity, 2)

    def calculate_wind_capacity(
        self,
        land_area: float,
        wind_score: float
    ) -> float:
        """
        Calculate recommended wind capacity in MW.
        """

        if land_area <= 0 or wind_score < self.wind_min_score:
            return 0.0

        maximum_capacity = (
            land_area / self.wind_acres_per_mw
        )

        resource_factor = wind_score / 100

        capacity = maximum_capacity * resource_factor

        return round(capacity, 2)

    def plan_capacity(
        self,
        site_details: Dict
    ) -> Dict:
        """
        Estimate capacity based on the selected deployment strategy.

        Expected input:

        {
            "land_area": 100,
            "solar_score": 85,
            "wind_score": 40,
            "deployment": "Solar"
        }
        """

        land_area = site_details.get("land_area", 0)
        solar_score = site_details.get("solar_score", 0)
        wind_score = site_details.get("wind_score", 0)
        deployment = site_details.get(
            "deployment",
            "Not Recommended"
        )

        solar_capacity = 0.0
        wind_capacity = 0.0

        if deployment in ["Solar", "Hybrid"]:
            solar_capacity = self.calculate_solar_capacity(
                land_area,
                solar_score
            )

        if deployment in ["Wind", "Hybrid"]:
            wind_capacity = self.calculate_wind_capacity(
                land_area,
                wind_score
            )

        total_capacity = (
            solar_capacity + wind_capacity
        )

        return {
            "deployment": deployment,
            "solar_capacity_mw": solar_capacity,
            "wind_capacity_mw": wind_capacity,
            "total_capacity_mw": round(
                total_capacity,
                2
            )
        }