# Calculate number of days between two given dates
from datetime import datetime

#2020-02-25
date_1 = datetime(2020, 2, 25).date()
#2020-09-17
date_2 = datetime(2020, 9, 17).date()

print(date_1,date_2)
print(date_2-date_1)

delta=None

if date_1>date_2:
    delta=date_1-date_2
else:
    delta=date_2-date_1

print("Difference of the days will be:\n",delta.days)