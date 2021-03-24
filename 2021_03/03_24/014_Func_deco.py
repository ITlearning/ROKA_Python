# 함수 데코레이터의 기본
def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    return wrapper
    

# 데코레이터를 붙여 함수를 만듭니다.
@test
def hello():
    print("hello")

    
hello()