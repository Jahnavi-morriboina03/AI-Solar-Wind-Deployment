
# backend/app/services/analysis_pipeline.py
from backend.app.services.solar_assessment import SolarAssessmentService
from backend.app.services.wind_assessment import classify_wind_site
from backend.app.evaluation.evaluator import EvaluationService
from backend.app.services.deployment_strategy import DeploymentStrategyService


class AnalysisPipeline:
    """
    Executes the complete analysis workflow.
    """

    def __init__(self):
        self.solar_service = SolarAssessmentService()
        self.evaluation_service = EvaluationService()
        self.deployment_service = DeploymentStrategyService()

    def analyze(self, features: dict):

        # Solar assessment
        solar_class = self.solar_service.classify_solar_site(
            features["solar_irradiance"]
        )

        # Wind assessment
        wind_result = classify_wind_site(
            features["wind_speed"]
        )

        # Site evaluation
        evaluation = self.evaluation_service.evaluate(features)

        # Deployment recommendation
        recommendation = self.deployment_service.generate_recommendation(
            solar_class,
            wind_result["wind_class"]
        )

        return {
            "solar": {
                "solar_class": solar_class
            },
            "wind": wind_result,
            "evaluation": evaluation,
            "deployment": recommendation
        }