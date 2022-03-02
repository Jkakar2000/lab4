hour = int(input('Enter the hour of the day'))
minute = int(input('Enter the minutes of the day'))
day = str(input("Enter AM or PM"))

hourSt = str(hour)
minuteSt = str(minute)

print("The time is " + hourSt + ":" + minuteSt + day)
if(day == 'PM'):
    hour = hour + 12
    hourSt = str(hour)
print("The time is in military " + hourSt + ":" + minuteSt + day)

