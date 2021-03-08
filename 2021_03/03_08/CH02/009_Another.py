# 대소문자 바꾸기
a = "Hello Python Programming"
print(a.upper())
print(a.lower())
# 비파괴적 함수임

# 문자열 양옆의 공백 제거하기
input_a = """ 
    안녕하세요
문자열의 함수를 알아봅시다
"""

print(input_a)

print(input_a.strip())


# 문자열의 구성 파악하기

print("TrainA10".isalpha())
print("10".isdigit())

# 문자열 찾기
output_a = "안녕안녕하세요".find("안녕") # 왼쪽부터 찾기 시작해서 처음 등장하는 위치를 반환
print(output_a)

output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)                       # 오른쪽부터 찾기 시작해서 처음 등장하는 위치를 반환

# 문자열과 in 연산자
print("안녕" in "안녕하세요")        # 안녕하세요 문자에 안녕 을 포함하고 있으면 True반환 아니면 False
print("잘자" in "안녕하세요")

# 문자열 자르기
a = "10;20;30;40;50".split(";") # split()에 있는 조건으로 문자열을 자른다 
print(a)
# 실행결과로 리스트(list)가 나온다.
