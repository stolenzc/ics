import datetime

from fastapi import FastAPI

from app.api import birthday, ics

# from app.core.config import settings

app = FastAPI(title="日程订阅管家", version="1.0")

# 注册API路由
app.include_router(birthday.router, prefix="/birthday", tags=["Birthday"])
app.include_router(ics.router, prefix="/ics", tags=["ICS"])


@app.get("/healthz")
async def root():
    return {"now": datetime.datetime.now()}
