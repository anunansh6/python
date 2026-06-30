import datetime


today = datetime.date.today()
print(today)

my_date = datetime.date(2024, 12, 25)
print(my_date)

my_date = datetime.datetime(2024, 12, 25, 10, 30)
print(my_date)

import time
time.time()

today+=datetime.timedelta(days=500)
print(today)




