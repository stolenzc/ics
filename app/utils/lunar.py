from datetime import date

from lunarcalendar import Converter, Lunar


def lunar_to_solar(year, month, day) -> date:
    """
    将农历日期(YYYY-MM-DD)转换为公历日期(YYYY-MM-DD)。
    """

    lunar = Lunar(year, month, day)
    solar = Converter.Lunar2Solar(lunar)
    return solar.to_date()
