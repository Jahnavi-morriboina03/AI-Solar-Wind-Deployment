from fastapi import APIRouter
from pydantic import BaseModel

from backend.app.services.analysis_pipeline import AnalysisPipeline

router = APIRouter(tags=["Analysis"])

pipeline = AnalysisPipeline()


class AnalysisRequest(BaseModel):
    solar_irradiance: float
    wind_speed: float
    slope: float
    distance_to_grid: float
    distance_to_road: float


@router.post("/analysis")
def analyze_site(request: AnalysisRequest):

    features = request.model_dump()

    result = pipeline.analyze(features)

    return result