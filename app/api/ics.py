from fastapi import APIRouter, Depends
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session

from app.crud.birthday import get_birthdays
from app.database.db import get_db
from app.utils.ics import generate_ics_content

router = APIRouter()


@router.get("/cal.ics", response_class=PlainTextResponse)
async def get_birthday_ics(db: Session = Depends(get_db)):
    """
    获取所有用户的生日信息，并返回一个符合 iCalendar 格式的 .ics 文件。
    """
    # 获取所有生日数据
    birthdays = get_birthdays(db)

    # 生成 iCalendar 格式的内容
    ics_content = generate_ics_content(birthdays)

    # 返回 .ics 内容
    return ics_content
