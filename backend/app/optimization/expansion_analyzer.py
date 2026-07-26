from typing import Dict


class ExpansionAnalyzer:
    """
    Analyzes whether a renewable energy site
    has future expansion potential based on
    optimization constraints.
    """

    def __init__(
        self,
        min_land_availability: float = 30.0,
        min_budget_ratio: float = 0.20,
        min_grid_capacity: float = 20.0,
        min_infrastructure_score: float = 50.0
    ):
        self.min_land_availability = (
            min_land_availability
        )

        self.min_budget_ratio = (
            min_budget_ratio
        )

        self.min_grid_capacity = (
            min_grid_capacity
        )

        self.min_infrastructure_score = (
            min_infrastructure_score
        )

    def analyze(
        self,
        site_details: Dict
    ) -> Dict:
        """
        Determine expansion feasibility based on
        optimization constraints.

        Expected input:

        {
            "available_land_area": 100,
            "required_land_area": 50,
            "available_budget": 10000000,
            "expansion_cost": 5000000,
            "environmental_restriction": False,
            "available_grid_capacity": 80,
            "infrastructure_score": 75
        }
        """

        available_land = site_details.get(
            "available_land_area",
            0
        )

        required_land = site_details.get(
            "required_land_area",
            0
        )

        available_budget = site_details.get(
            "available_budget",
            0
        )

        expansion_cost = site_details.get(
            "expansion_cost",
            0
        )

        environmental_restriction = (
            site_details.get(
                "environmental_restriction",
                False
            )
        )

        available_grid_capacity = (
            site_details.get(
                "available_grid_capacity",
                0
            )
        )

        infrastructure_score = (
            site_details.get(
                "infrastructure_score",
                0
            )
        )

        constraints = {
            "land": self._check_land(
                available_land,
                required_land
            ),

            "budget": self._check_budget(
                available_budget,
                expansion_cost
            ),

            "environment": (
                not environmental_restriction
            ),

            "grid": (
                available_grid_capacity
                >= self.min_grid_capacity
            ),

            "infrastructure": (
                infrastructure_score
                >= self.min_infrastructure_score
            )
        }

        passed_constraints = sum(
            constraints.values()
        )

        total_constraints = len(
            constraints
        )

        if (
            constraints["environment"]
            and passed_constraints == total_constraints
        ):
            status = "Expandable"

        elif passed_constraints >= 3:
            status = "Limited Expansion"

        else:
            status = "Not Expandable"

        return {
            "expansion_status": status,
            "constraints": constraints,
            "passed_constraints": passed_constraints,
            "total_constraints": total_constraints
        }

    def _check_land(
        self,
        available_land: float,
        required_land: float
    ) -> bool:
        """
        Check whether sufficient land is available.
        """

        if available_land <= 0:
            return False

        if required_land <= 0:
            return False

        remaining_land = (
            available_land - required_land
        )

        return (
            remaining_land
            >= self.min_land_availability
        )

    def _check_budget(
        self,
        available_budget: float,
        expansion_cost: float
    ) -> bool:
        """
        Check whether the expansion is affordable.
        """

        if available_budget <= 0:
            return False

        if expansion_cost <= 0:
            return False

        remaining_budget = (
            available_budget - expansion_cost
        )

        minimum_remaining_budget = (
            available_budget
            * self.min_budget_ratio
        )

        return (
            remaining_budget
            >= minimum_remaining_budget
        )