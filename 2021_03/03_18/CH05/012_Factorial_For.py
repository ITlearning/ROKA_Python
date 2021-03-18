# 재귀함수
# 팩토리얼을 사용

# 반복문으로 팩토리얼 구하기

def factorial(n) :
    output = 1 # 어떤 값이라도 1을 곱하면 변화가 없기 때문에 1로 설정한 것이다.
    for i in range(1,n+1) :
        output *= i
    return output

print("1!: ", factorial(1))
print("2!: ", factorial(2))
print("3!: ", factorial(3))
print("4!: ", factorial(4))
print("5!: ", factorial(5))