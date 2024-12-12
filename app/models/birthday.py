from datetime import date, datetime

from sqlalchemy import Boolean, Date, DateTime, Integer, String, text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.db import Base


class Birthday(Base):
    __tablename__ = 'birthday'  # 表名使用单数形式

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30))
    birthday: Mapped[date] = mapped_column(Date, nullable=False, comment="生日日期")
    is_lunar: Mapped[bool] = mapped_column(
        Boolean, default=False, comment="是否是农历", server_default=text("0")
    )
    is_remind: Mapped[bool] = mapped_column(
        Boolean, default=True, comment="是否提醒", server_default=text("1")
    )
    create_time: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(), server_default=text("NOW()")
    )
    update_time: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(),
        onupdate=datetime.now(),
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )
    is_delete: Mapped[bool] = mapped_column(Boolean, default=False, server_default=text("0"))
