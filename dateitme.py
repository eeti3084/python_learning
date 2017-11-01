import datetime

# d=datetime.date(2016,7,24)
# print(d)

td=datetime.date.today()
# print(td.day)
# print(td.weekday())
# print(td.isoweekday())

#time delta
tdelta=datetime.timedelta(days=7)
print(td+tdelta)
print(td-tdelta)

bday=datetime.date(2018,3,30)

till_bday=bday-td
print(till_bday.total_seconds())

t=datetime.datetime(2017,10,22,9,30,45,100000)
print(t)

