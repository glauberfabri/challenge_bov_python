from datetime import datetime

def is_bonus_applicable(volume):
    return volume > 10000

def get_semester(date):
    month = datetime.strptime(date, "%Y-%m-%d").month
    return "first" if 1 <= month <= 6 else "second"