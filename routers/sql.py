from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

import utils.sql as sql_utils

router = APIRouter(prefix="/sql", tags=["sql"])


@router.get("/health_check")
async def check_health(db: Session = Depends(sql_utils.get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "OK"}
    except OperationalError as e:
        return {"status": "ERROR", "detail": str(e)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
