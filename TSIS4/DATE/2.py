import datetime
today = datetime.date.today()
 yesterday = datetime.date.today()-datetime.timedelta(days = 1) 
tomorrow = datetime.date.today()+datetime.timedelta(days= 1)

print("Today's date is",today)
print("Yesterday's date is",yesterday)
print("Tomorrow's date is",tomorrow)
