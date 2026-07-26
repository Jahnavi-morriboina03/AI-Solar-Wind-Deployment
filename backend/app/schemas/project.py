from pydantic import BaseModel,Field
from datetime import datetime

class ProjectCreate(BaseModel):
    project_name: str= Field(..., min_length=1)
    description: str
    state: str
    latitude: float
    longitude: float


class ProjectResponse(ProjectCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True