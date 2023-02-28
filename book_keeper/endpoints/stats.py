from fastapi import Depends, APIRouter
from sqlalchemy import text
from sqlalchemy.orm import Session

from database.config import get_db
from database.models import StatsModel

stats_router = APIRouter()


@stats_router.put("/")
def calculate_stats(db: Session = Depends(get_db)):
    payload = {}
    for sql_query in dir(StatsModel):
        if sql_query.startswith("sql_"):  # useful class attributes (later file names) start with 'sql_'
            try:
                with open(f".\\sql_queries\\{sql_query}.sql") as file:
                    raw_sql = file.read()
                query_result = db.execute(text(raw_sql)).all()
                payload[sql_query] = str(query_result)
            except FileNotFoundError:
                payload[sql_query] = "Unknown"

    new_stats = StatsModel(**payload)
    db.add(new_stats)
    db.commit()
    db.refresh(new_stats)
    return new_stats


@stats_router.get("/")
def get_stats(db: Session = Depends(get_db)):
    return db.query(StatsModel).order_by(StatsModel.calculated_at.desc()).all()
