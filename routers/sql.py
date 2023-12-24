from fastapi import APIRouter
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker

import utils.env as env

router = APIRouter(prefix="/sql", tags=["sql"])


@router.get("/health_check")
async def check_health():
    try:
        engine = create_engine(env.SQLALCHEMY_DATABASE_URL, echo=True)
        Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
        session = Session()
        session.execute(text("SELECT 1"))
        return {"status": "OK"}
    except OperationalError as e:
        return {"status": "Error", "message": str(e)}
