import uvicorn
from fastapi import FastAPI

from database import models
from database.config import engine
from endpoints import book

if __name__ == '__main__':
    models.Base.metadata.create_all(bind=engine)
    app = FastAPI()
    app.include_router(book.router, tags=['stats'], prefix='/api/stats')

    uvicorn.run(app, host="0.0.0.0", port=8001)
