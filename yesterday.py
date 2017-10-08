import datetime
#today = datetime.date.today()
today = datetime.datetime.now()
oneday = datetime.timedelta(days=1)
yesterday = today - oneday
print yesterday;

