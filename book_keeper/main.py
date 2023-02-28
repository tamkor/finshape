import uvicorn
from fastapi import FastAPI

from database import models
from database.config import engine
from endpoints import book, stats

routes = {
    "books": "/api/books",
    "stats": "/api/stats",
}
HOST = "localhost"
PORT = 8000

if __name__ == '__main__':
    models.Base.metadata.create_all(bind=engine)
    app = FastAPI()
    app.include_router(book.book_router, tags=['Books'], prefix=routes["books"])
    app.include_router(stats.stats_router, tags=['Stats'], prefix=routes["stats"])

    uvicorn.run(app, host=HOST, port=PORT)
