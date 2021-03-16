# 가변 매개변수 함수
# print() 함수와 같이 매개변수를 원하는 만큼 받을 수 있는 함수.

# 사용할때의 제약
# 1. 가변 매개변수 뒤에는 일반 매개변수가 올 수 없다.
# 2. 가변 매개변수는 하나만 사용이 가능하다.

def print_n_times(n, *values) :
    for i in range(n) :
        for value in values :
            print(value)
        print() # 단순 줄바꿈
    
print_n_times(3, "안녕하세요", "반갑습니다", "즐겁습니다")

# value는 리스트처럼 활용이 된다. 따라서 for 문을 중첩하여 하나씩 출력되게 한다. 