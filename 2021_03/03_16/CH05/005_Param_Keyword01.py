# 키워드 매개변수
# value를 여러 개 입력할 수 있으므로 가변 매개변수를 앞에 두고, 뒤에 기본 매개변수들이 들어가 있는 형태이다.

def print_n_times(*values, n = 2) :
    for i in range(n) :
        for value in values :
            print(value)
        print()

print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)
# 이처럼 매개변수 이름을 지정해서 입력하는 매개변수를 키워드 매개변수라고 부른다.