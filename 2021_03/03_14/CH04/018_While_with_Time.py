# while 반복문: 시간을 기반으로 반복하기

# 5초 동안 반복하기
# 시간과 관련된 기능을 가져옵니다.
import time

number = 0

# 5초 동안 반복됩니다.
target_tick = time.time() + 5
while time.time() < target_tick :
    number += 1
    
# 출력합니다.
print("5초동안 {}번 반복했습니다.".format(number))