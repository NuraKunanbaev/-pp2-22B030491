import datetime

today = datetime.date.today()-datetime.timedelta(days=5)  #timedelta - разница между датами

print("Date after subtracting 5 days:",today)