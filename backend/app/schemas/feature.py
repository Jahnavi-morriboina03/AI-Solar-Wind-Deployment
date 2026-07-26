from pydantic import BaseModel
from datetime import datetime


class FeatureCreate(BaseModel):
    latitude: float
    longitude: float
    solar_irradiance: float
    wind_speed: float
    temperature: float
    humidity: float
    elevation: float
    slope: float


class FeatureResponse(BaseModel):
    id: int
    latitude: float
    longitude: float
    solar_irradiance: float
    wind_speed: float
    temperature: float
    humidity: float
    elevation: float
    slope: float
    created_at: datetime

    class Config:
        from_attributes = True