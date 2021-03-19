# 함수의 매개 변수로 함수 전달하기

def call_10_times(func) :
    for i in range(10) :
        func()
        
        
def print_hello() :
    print("안녕하세요")
    
    
call_10_times(print_hello)
# 매개변수로 함수를 전달합니다.

# 프로그램을 실행하면 print_hello() 함수를 10번 실행한다.