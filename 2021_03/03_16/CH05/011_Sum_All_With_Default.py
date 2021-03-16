# 기본 매개변수와 키워드 매개변수를 활용해 범위의 정수를 더하는 함수
def sum_all(start = 0, end = 100, step = 1) :
    output = 0
    for i in range(start,end + 1, step) :
        output += i
    return output

print("A. ", sum_all(0,100,10))
print("B. ", sum_all(end = 100))
print("C. ", sum_all(end = 100, step = 2))