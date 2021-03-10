# 리스트에 요소 추가하기
# 파괴적 처리 함수
# append(), insert(), extend()

# 리스트를 선언합니다
list_a = [1,2,3]

# 리스트 뒤에 요소 추가하기
print('# 리스트 뒤에 요소 추가하기')
list_a.append(4)
list_a.append(5)
print(list_a)
print()

# 리스트 중간에 요소 추가하기
print('# 리스트 중간에 요소 추가하기')
list_a.insert(0,10) # 0 번째 배열에 10 추가하기
print(list_a)

# 한번에 여러 요소 추가하기
print('# 한번에 여러 요소 추가하기')
list_a.extend([4,5,6]) # extend는 파괴적 처리다. 반면 list_a + list_b 의 경우 단순히 연결만하고 하나하나의 리스트에는 타격이 가지 않는다.
print(list_a)