# 자료 없이 리턴하기
# 함수 내부에서는 return이라는 키워드를 사용할 수 있다.
# 이 키워드는 함수를 실행했던 위치로 돌아가라는 뜻으로, 함수가 끝나는 위치를 의미한다.

def return_test() :
    print("A 위치입니다.")
    return
    print("B 위치입니다.")
    
return_test()