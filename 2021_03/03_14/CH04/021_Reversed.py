# reversed() 함수

# 리스트를 선언하고 뒤집습니다.
list_a = [1,2,3,4,5]
list_reversed = reversed(list_a)

# 출력합니다.
print("# reversed 함수")
print("reversed(list_a) : ", list_reversed)
print("list(reversed(list_a)) : ", list(list_reversed))
print()

# 반복문을 적용합니다.
print("# reversed() 함수와 반복문")
print("for i in reversed(list_a) : ")
for i in reversed(list_a) :
    print("-", i)
    
# 확장 슬라이싱
# 비파괴적 코드이다.
print(list_a[::-1])