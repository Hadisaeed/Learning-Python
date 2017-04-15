import datetime
now=datetime.datetime.now()
current_date=now.strftime("%d-%m-%y")
print('Date is: ',current_date)
current_time=now.strftime("%H:%M:%S")
print("Current Time is: ", current_time)