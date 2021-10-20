from datetime import datetime

# current date and time
now = datetime.now()

# current time
nowtime = now.time()
print(nowtime)

# link time
link_time = nowtime.replace(hour=8, minute=0, second=0, microsecond=0)
print(link_time)

#current date
nowdate = now.date()
print(nowdate.weekday())