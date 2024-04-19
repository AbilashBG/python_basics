
# Date Time in Python
import datetime as dt
 
current_date = dt.date.today()
print("Current Date : ", current_date)
 
new = dt.date(2021, 10, 25)
print(new)
print("Year : ", new.year)
print("Month : ", new.month)
print("Day : ", new.day)
print("--------------------------------------")

# output

# Current Date :  2022-03-25
# 2021-10-25
# Year :  2021
# Month :  10
# Day :  25
# --------------------------------------

a = dt.time(10, 45, 5, 555505)
print(a)
print("Hour : ", a.hour)
print("minute : ", a.minute)
print("second : ", a.second)
print("microsecond : ", a.microsecond)
print("--------------------------------------")

# output

# 10:45:05.555505
# Hour :  10
# minute :  45
# second :  5
# microsecond :  555505
# --------------------------------------

current_time = dt.datetime.now()
print("Current Time : ", current_time)
print("--------------------------------------")

# output

# Current Time :  2022-03-25 12:12:56.376654
# --------------------------------------
new = dt.datetime(2021, 5, 31, 12, 2, 10)
print(new)
print(new.date())
print(new.time())
print("--------------------------------------")

# output

# 2021-05-31 12:02:10
# 2021-05-31
# 12:02:10
# --------------------------------------

current = dt.datetime.now()
new_year = dt.datetime(2022, 1, 1)
difference = new_year - current
print(difference)
print("--------------------------------------")

# output

# -84 days, 11:47:03.621624
# --------------------------------------

current = dt.datetime.now()
print(current)
s=current.strftime("%A %b %d %Y")
print(s)

# output

# 2022-03-25 12:12:56.378856
# Friday Mar 25 2022
