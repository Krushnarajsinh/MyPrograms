#TODO:You are given a date. Your task is to find what the day is on that date.
import calendar
m,d,y=input().split()
week_days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
day=calendar.weekday(int(y),int(m),int(d))
#print(day)
print(week_days[day])
