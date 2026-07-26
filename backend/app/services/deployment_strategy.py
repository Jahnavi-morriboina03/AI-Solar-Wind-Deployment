

from backend.app.services.hybrid_recommendation import (
    recommend_hybrid_strategy
)


class DeploymentStrategyService:

    def recommend_deployment(
        self,
        solar_class: str,
        wind_class: str
    ) -> str:

        return recommend_hybrid_strategy(
            solar_class,
            wind_class
        )

    def generate_reason(
        self,
        solar_class: str,
        wind_class: str
    ) -> str:

        deployment = self.recommend_deployment(
            solar_class,
            wind_class
        )

        if deployment == "Hybrid":
            return (
                "High solar irradiance and consistently strong "
                "wind resource."
            )

        elif deployment == "Solar":
            return (
                "Strong solar irradiance makes solar deployment "
                "the most suitable option."
            )

        elif deployment == "Wind":
            return (
                "Strong wind resource makes wind deployment "
                "the most suitable option."
            )

        else:
            return (
                "Both solar and wind resources are insufficient "
                "for a strong deployment recommendation."
            )

    def confidence_score(
        self,
        solar_class: str,
        wind_class: str
    ) -> int:

        score_map = {
            "Poor": 25,
            "Moderate": 50,
            "Good": 75,
            "Excellent": 95
        }

        solar_score = score_map[solar_class]
        wind_score = score_map[wind_class]

        deployment = self.recommend_deployment(
            solar_class,
            wind_class
        )

        if deployment == "Hybrid":
            return round(
                (solar_score + wind_score) / 2
            )

        elif deployment == "Solar":
            return solar_score

        elif deployment == "Wind":
            return wind_score

        return 20

    def generate_recommendation(
        self,
        solar_class: str,
        wind_class: str
    ) -> dict:

        deployment = self.recommend_deployment(
            solar_class,
            wind_class
        )

        confidence = self.confidence_score(
            solar_class,
            wind_class
        )

        reason = self.generate_reason(
            solar_class,
            wind_class
        )

        return {
            "deployment": deployment,
            "confidence": confidence,
            "reason": reason
        }