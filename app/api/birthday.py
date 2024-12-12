from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.birthday import create_birthday, delete_birthday, get_birthdays
from app.database.db import get_db
from app.schemas.birthday import BirthdayCreate, BirthdayResponse

router = APIRouter()


@router.post("/", response_model=BirthdayResponse, status_code=201)
async def add_birthday(birthday: BirthdayCreate, db: Session = Depends(get_db)):
    return create_birthday(db, birthday)


@router.get("/", response_model=list[BirthdayResponse])
async def list_birthdays(db: Session = Depends(get_db)):
    return get_birthdays(db)


@router.delete("/{birthday_id}", status_code=204)
async def remove_birthday(birthday_id: int, db: Session = Depends(get_db)):
    return delete_birthday(db, birthday_id)
