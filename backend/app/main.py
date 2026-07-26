#Import FastApi
from fastapi import FastAPI

from backend.app.database.database import engine, Base
from backend.app.models.project import Project
from backend.app.models.feature import Feature


from backend.app.api.home import router as home_router
from backend.app.api.projects import router as projects_router
from backend.app.api.sites import router as sites_router
from backend.app.api.predictions import router as predictions_router
from backend.app.api.feature import router as features_router
from backend.app.api.solar import router as solar_router


#create Fstapi application
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(home_router)
app.include_router(projects_router)
app.include_router(sites_router)
app.include_router(predictions_router)
app.include_router(features_router)
app.include_router(solar_router)
#Home endpoint
#@app.get("/")
#def home():
#    return {
   #     "message": "Solar & Wind Deployment Intelligence Platform"
 #   }

