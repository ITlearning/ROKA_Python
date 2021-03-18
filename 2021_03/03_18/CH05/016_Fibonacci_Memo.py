# 메모화

# 메모 변수를 만듭니다.
dic = {
    1: 1,
    2: 1
}

def fibonacci(n) :
    if n in dic :
        # 메모가 되어있으면 메모된 값을 리턴
        return dic[n]
    else :
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dic[n] = output
        return output
    
print("fibonacci(10): ", fibonacci(10))
print("fibonacci(20): ", fibonacci(20))
print("fibonacci(30): ", fibonacci(30))
print("fibonacci(40): ", fibonacci(40))
print("fibonacci(50): ", fibonacci(50))