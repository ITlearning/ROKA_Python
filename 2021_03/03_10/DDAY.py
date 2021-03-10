import datetime

time = datetime.date.today() # 현재 날짜

day = datetime.date(2021,5,16) # 전역일

value = day - time # D-Day

print(value.days)