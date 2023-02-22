import datetime
dt1 = datetime.datetime.today().replace(microsecond = 0)
dt2 = datetime.datetime(2006, 2, 21, hour=5, minute=38, second=25, microsecond=0, tzinfo=None)
def difference(dt1, dt2):
    dif = dt1 - dt2
    return dif.days*24*3600 + dif.seconds
print(difference(dt1, dt2))

