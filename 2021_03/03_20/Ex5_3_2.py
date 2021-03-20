numbers = list(range(1,10 + 1))

print("# 홀수만 출력하기")
print(list(filter(lambda x: x % 2 == 0, numbers)))
print()

print("# 3 이상, 7미만 추출하기")
print(list(filter(lambda x: 3 < x < 7, numbers)))
print()

print("# 제곱해서 50 미만 출력하기")
print(list(filter(lambda x: x*x < 50, numbers)))