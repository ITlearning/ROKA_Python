# 이터레이터
# '반복할 수 있는 것'을 프로그래밍 용어로 이터러블 이라고 합니다.
# 즉 이터러블은 내부에 있는 요소들을 차례차례 꺼낼 수 있는 객체를 의미한다.

# 리스트, 딕셔너리, 문자열 튜플, 등 모두 내부에서 요소를 차례차례 꺼낼 수 있으므로 이터러블이다.

# 이터러블 중에서 next() 함수를 적용해 하나하나 꺼낼 수 있는 요소를 이터레이터 라고 한다.

numbers = [1,2,3,4,5,6]
r_num = reversed(numbers)

print("reversed_numbers = ", r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))