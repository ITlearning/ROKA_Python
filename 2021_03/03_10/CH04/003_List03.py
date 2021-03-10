# 리스트 연결 연산자와 요소 추가의 차이
# del 방법과 pop 방법

list_a = [0,1,2,3,4,5]
print('# 리스트 요소 하나 제거하기')

# 제거 방법[1] - del
del list_a[1]

print("del list_a[1] : ", list_a)

# 제거 방법[2] - pop()
list_a.pop(2) # 매개변수로 아무것도 입력하지 않으면, 가장 뒤쪽에 있는 숫자가 제거 된다.
print("pop(2) : ", list_a)


# 값으로 제거하기

list_c = [1,2,1,2]
list_c.remove(2)  # 리스트의 요소를 값으로 제거하기 
list_c.remove(2)  # 내부에 여러개가 있어도 가장 먼저 발견되는 하나만 제거한다.
print(list_c)

# 모두 제거하기
list_c.clear()
print(list_c)