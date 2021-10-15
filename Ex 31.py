import datetime
now = datetime.datetime.now()


# for current_date
def current_date():
    current_date = now.strftime('%y/%m/%d')  # %y = year, %m = Month, %d = Day
    return current_date


# for time_date
def current_time():
    current_time = now.strftime('%H:%M:%S')  # %H = Hours, %M = Minute, %S = Second
    return current_time


print(current_time())
print(type(current_time()))

print('=='*10)

print(current_date())
print(type(current_date()))
