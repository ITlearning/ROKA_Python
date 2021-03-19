# 재귀 함수로 구현한 피보나치 수열(2)
counter = 0

def fibonacci(n) :
    global counter
    # 파이썬은 함수 내부에서 함수 외부에 있는 변수를 참조하지 못한다.
    # 그래서 함수 내부에서 함수 외부에 있는 변수라는 것을 설명하려면 다음과 같은 구문을 사용한다.
    counter += 1
    if n == 1 :
        return 1
    elif n == 2 :
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)
    
print("fibonacci(10): ", fibonacci(10))
print("fibonacci(10)계산에 활용된 덧셈 횟수는 {}번입니다".format(counter))