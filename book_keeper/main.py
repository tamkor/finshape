import uvicorn
import os
from fastapi import FastAPI

from db_access import models
from db_access.config import engine
from endpoints import book

routes = {
    "books": "/api/books",
    "stats": "/api/stats",
}

if __name__ == '__main__':
    models.Base.metadata.create_all(bind=engine)
    app = FastAPI()
    app.include_router(book.book_router, tags=['Books'], prefix=routes["books"])

    uvicorn.run(app, host=os.getenv("BKHOST"), port=int(os.getenv("BKPORT")))
