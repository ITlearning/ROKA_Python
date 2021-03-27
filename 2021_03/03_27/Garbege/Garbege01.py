# 가비지 컬렉터 : 변수에 저장하지 않은 경우
class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다.".format(self.name))
    def __del__(self):
        print("{} - 파괴되었습니다.".format(self.name))
        
Test("A")
Test("B")
Test("C")

# 이 테스트는 변수에 저장하지 않은 채로 실행되는 경우이다.
# 변수에 저장되지 않았을 경우에는 . 가비지 컬렉터는 이후에 활용하지 않겠다는 의미로 이해하고 메모리를 아끼기 위해 과감히 지워버린다.