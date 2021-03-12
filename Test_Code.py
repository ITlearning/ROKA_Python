# 테스트 페이지입니다.
# 약간의 실습이나 문제가 생겼을 경우 사용합니다.

numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers :
    if number in counter :
        counter[number] = counter[number] + 1
    else :
        counter[number] = 1

    
print(counter)