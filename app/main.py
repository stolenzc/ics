import datetime

from fastapi import APIRouter, FastAPI

from app.api import birthday, ics

# from app.core.config import settings

app = FastAPI(title="日程订阅管家", version="1.0")

# 注册API路由
root_router = APIRouter(prefix="/ics")
root_router.include_router(birthday.router, prefix="/birthday", tags=["Birthday"])
root_router.include_router(ics.router, prefix="/cal.ics", tags=["Subscribe To ICS"])

app.include_router(root_router)


@app.get("/healthz")
async def root():
    return {"now": datetime.datetime.now()}
