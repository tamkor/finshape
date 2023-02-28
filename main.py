import uvicorn
from fastapi import FastAPI

import book
import models
from database import engine

if __name__ == '__main__':
    models.Base.metadata.create_all(bind=engine)
    app = FastAPI()
    app.include_router(book.router, tags=['Books'], prefix='/api/books')

    uvicorn.run(app, host="0.0.0.0", port=8000)
