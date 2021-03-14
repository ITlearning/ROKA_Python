# while 반복문 : 상태를 기반으로 반복하기

# 해당하는 값 모두 제거하기
# 변수를 선언합니다
list_test = [1,2,1,2]
value = 2

while value in list_test :
    list_test.remove(value)
    
print(list_test)