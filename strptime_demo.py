import datetime
dtstr = '2014-02-14 21:32:12'
tmp=datetime.datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S").date()
print tmp;

#tmp=datetime.date(2014, 2, 14)
