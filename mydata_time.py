import datetime

now = datetime.datetime.now()
print(f"current time: {now}")
date_1 = datetime.datetime(2019, 5, 10,12,1,1)
print(f"specific time: {date_1}")
time_to_string = now.strftime("%Y-%m-%d %H:%M:%S")  # strftime: string from time
print(f"date to string: {time_to_string}")
str = "2020-01-01 1:10:11"
string_to_time = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
print(f"string to date: {string_to_time}")