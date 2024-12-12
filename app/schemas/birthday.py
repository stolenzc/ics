from datetime import date

from pydantic import BaseModel


class BirthdayCreate(BaseModel):
    name: str
    birthday: date | None = None
    is_lunar: bool = False


class BirthdayResponse(BirthdayCreate):
    id: int

    class Config:
        from_attributes = True  # 使 Pydantic 识别SQLAlchemy模型
