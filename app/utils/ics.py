from datetime import date, datetime
from typing import List

from icalendar import Calendar, Event

from app.models.birthday import Birthday
from app.utils.lunar import lunar_to_solar


def generate_ics_content(birthdays: List[Birthday]) -> str:
    calendar = Calendar()

    for birthday in birthdays:
        born_date = birthday.birthday
        for year in range(born_date.year, 2051):
            event = Event()

            if birthday.is_lunar:
                celebrate_date = lunar_to_solar(year, born_date.month, born_date.day)
            else:
                celebrate_date = date(year, born_date.month, born_date.day)

            event.add('summary', f"{birthday.name}的第{year - born_date.year}岁生日")
            event.add('dtstart', datetime.combine(celebrate_date, datetime.min.time()))
            event.add('dtend', datetime.combine(celebrate_date, datetime.max.time()))

            calendar.add_component(event)

    return calendar.to_ical().decode('utf-8')
