# 날짜/ 시간을 한 줄로 출력하기

import datetime

now = datetime.datetime.now()

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

# 파이썬은 다른 언어와 다르게 날짜를 출력할때 3월이면 3을 출력한다. 인덱스가 0부터 시작하는게 아니라 이거임 ㅇㅇ