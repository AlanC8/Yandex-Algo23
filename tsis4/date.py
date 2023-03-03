import datetime
x = datetime.datetime.now()
y = datetime.datetime(x.year, x.month, x.day - 5)
print(y.strftime("%x"))

x1 = datetime.datetime.now()
print(x1.day - 1, x1.day, x1.day + 1)

x2 = datetime.datetime.today().replace(microsecond=0)
print(x2)

x3 = datetime.datetime.now()
year = int(input())
month = int(input())
day = int(input())

if (x3.year != year):
    year_time = ((x3.year - year) * 365 * 24 * 60)
elif (x3.year == year):
    year_time = 0

if (x3.month != month):
    month_time = ((x3.month - month) * 30 * 24 * 60)
elif (x3.month == month):
    month_time = 0

if (x3.day != day):
    day_time = ((x3.day - day) * 24 * 60)
elif (x3.day == day):
    day_time = 0

calc = ((day_time + month_time + year_time) * 60) + x3.minute * 60
print(calc)
