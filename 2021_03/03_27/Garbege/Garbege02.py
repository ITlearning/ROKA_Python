# 가비지 컬렉터: 변수에 저장한 경우
class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다.".format(self.name))
    def __del__(self):
        print("{} - 파괴되었습니다.".format(self.name))
        
        
a = Test("A")
b = Test("B")
c = Test("C")

# 이번에는 변수에 저장을 했다.
# 변수에 저장을 하게될 경우에는, 가비지 컬렉터는 이 변수를 사용할 수도 있다라는 생각을 하기 때문에, 프로그램이 종료되기 전까지 계속 파괴시키지 않고 있다가
# 종료가 될 때 순서대로 파괴한다.