import uvicorn
import os
from fastapi import FastAPI

from db_access import models
from db_access.config import engine
from endpoints import stats

routes = {
    "stats": "/api/stats",
}

if __name__ == '__main__':
    models.Base.metadata.create_all(bind=engine)
    app = FastAPI()
    app.include_router(stats.stats_router, tags=['Stats'], prefix=routes["stats"])

    uvicorn.run(app, host=os.getenv("STATSHOST"), port=int(os.getenv("STATSPORT")))
