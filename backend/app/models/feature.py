from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime

from backend.app.database.database import Base


class Feature(Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True, index=True)

    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    solar_irradiance = Column(Float, nullable=True)
    wind_speed = Column(Float, nullable=True)
    temperature = Column(Float, nullable=True)
    humidity = Column(Float, nullable=True)

    elevation = Column(Float, nullable=True)
    slope = Column(Float, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)