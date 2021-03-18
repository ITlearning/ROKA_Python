# 재귀 함수로 구현한 피보나치 수열(1)
def fibonacci(n) :
    if n == 1 :
        return 1
    elif n == 2 :
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)
    
print("fibonacci(1): ", fibonacci(1))
print("fibonacci(2): ", fibonacci(2))
print("fibonacci(3): ", fibonacci(3))
print("fibonacci(4): ", fibonacci(4))
print("fibonacci(5): ", fibonacci(5))