import pandas as pd
from dateutil import parser
import datetime

moldova_holidays = {
    "New Year's Day": "01.01",  # Format: dd.mm.yyyy
    "International Women's Day": "08.03",
    "Mărțișor (Spring Day)": "01.03",
    "Labour Day": "01.05",
    "Europe Day": "09.05",
    "Independence Day": "27.08",
    "Limba Noastră (Language Day)": "31.08",
    "National Wine Day": "03.10",
    "Christmas Day": "25.12",
    "Orthodox Easter": "Varies (April or May)",
    "Orthodox Christmas Day": "07.01",
    "Orthodox Epiphany (Boboteaza)": "19.01",
    "Orthodox Good Friday": "Varies (Friday before Easter)",
    "Orthodox Ascension Day": "Varies (40 days after Easter)",
    "Orthodox Pentecost (Rusaliile)": "Varies (49 days after Easter)",
    "International Workers' Day": "01.05",
    "Victory and Commemoration Day": "09.05",
    "National Flag Day": "27.04",
    "Children's Day": "01.06",
    "National Army Day": "06.04",
    "Customs Service Day": "23.01",
    "Constitution Day": "29.07",
    "Teacher's Day": "05.10",
    "Police Day": "05.04",
    "Customs Officers Day": "27.05",
    "National Day of Mourning (for war victims)": "22.06",
    "National Environmental Day": "04.06",
    "National Day of Rural Women": "15.10",
    "Moldovan Language (Literacy) Day": "14.04",
    "National Day of Students": "17.12",
}

def isWorkDay(date):
    
    if date.weekday() < 5:
        return True
    else: 
        return False
    
def isHoliday(date):
    month_day = date.strftime("%d.%m")
    
    if month_day in moldova_holidays.values():
        return True
    else:
        return False

    
    
def classify_day(date_str):
    date = parser.parse(date_str).date()
    
    is_workday = isWorkDay(date)
    
    is_holiday = isHoliday(date)
    
    return is_workday, is_holiday    
    
def daysTillWeekend(start_date):
    date = parser.parse(start_date).date()
    days_until_weekend = 0

    while not isWorkDay(date):
        date += datetime.timedelta(days=1)
        days_until_weekend += 1

    return days_until_weekend

def daysTillHoliday(start_date):
    date = parser.parse(start_date).date()
    days_until_holiday = 0
    
    while not isHoliday(date):
        date += datetime.timedelta(days=1)
        days_until_holiday += 1
    
    return days_until_holiday
