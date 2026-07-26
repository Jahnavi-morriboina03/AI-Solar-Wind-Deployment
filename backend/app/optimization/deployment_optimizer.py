from typing import Dict


class DeploymentOptimizer:
    """
    Determines the most suitable renewable energy deployment strategy
    based on evaluated site details.
    """

    def __init__(
        self,
        solar_threshold: float = 70,
        wind_threshold: float = 70,
        hybrid_threshold: float = 70
    ):
        self.solar_threshold = solar_threshold
        self.wind_threshold = wind_threshold
        self.hybrid_threshold = hybrid_threshold

    def optimize(self, site_details: Dict) -> Dict:
        """
        Determine the best deployment strategy.

        Expected input:
        {
            "solar_score": 85,
            "wind_score": 40
        }
        """

        solar_score = site_details.get("solar_score", 0)
        wind_score = site_details.get("wind_score", 0)

        if (
            solar_score >= self.hybrid_threshold
            and wind_score >= self.hybrid_threshold
        ):
            deployment = "Hybrid"

        elif solar_score >= self.solar_threshold:
            deployment = "Solar"

        elif wind_score >= self.wind_threshold:
            deployment = "Wind"

        else:
            deployment = "Not Recommended"

        return {
            "deployment": deployment,
            "solar_score": solar_score,
            "wind_score": wind_score
        }