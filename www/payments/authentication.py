from datetime import datetime

time_passed_in_seconds =  datetime.utcnow() - datetime(2022, 12, 28, 23, 55, 59, 342380).astimezone().replace(tzinfo=None)
print(time_passed_in_seconds.total_seconds())