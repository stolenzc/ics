from datetime import datetime

from lunarcalendar import Converter, Lunar


def lunar_to_solar(year, month, day) -> datetime:
    """
    将农历日期(YYYY-MM-DD)转换为公历日期(YYYY-MM-DD)。
    """

    lunar = Lunar(year, month, day)
    solar = Converter.Lunar2Solar(lunar)
    return datetime.combine(solar.to_date(), datetime.min.time())
