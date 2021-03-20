# 제네레이터 함수

# 제네레이터는 파이썬의 특수한 문법 구조이다.
# 제네레이터는 이터레이터를 직접 만들 때 사용하는 코드이다.
# 함수 내부에 yield 키워드를 사용하면 해당 함수는 제네레이터 함수가 되며, 일반 함수와는 달리 함수를 호출해도 내부의 코드가 실행되지 않는다.

def test() :
    print("함수가 호출되었습니다.")
    yield "test"
    
print("A지점 통과")
test()

print("B지점 통과")
test()
print(test())