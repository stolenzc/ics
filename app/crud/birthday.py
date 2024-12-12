from sqlalchemy.orm import Session

from app.models.birthday import Birthday
from app.schemas.birthday import BirthdayCreate


def create_birthday(db: Session, birthday: BirthdayCreate):
    db_birthday = Birthday(
        name=birthday.name, birthday=birthday.birthday, is_lunar=birthday.is_lunar
    )
    db.add(db_birthday)
    db.commit()
    db.refresh(db_birthday)
    return db_birthday


def get_birthdays(db: Session):
    return db.query(Birthday).all()


def delete_birthday(db: Session, birthday_id: int):
    db_birthday = db.query(Birthday).filter(Birthday.id == birthday_id).first()
    if db_birthday:
        db.delete(db_birthday)
        db.commit()
        return db_birthday
    return None
