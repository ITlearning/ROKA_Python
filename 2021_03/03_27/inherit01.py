# 상속의 활용
class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init()__ 메소드가 호출되었습니다.")
    def test(self):
        print("Parent 클래스의 test() 메소드 입니다.")
        
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child 클래스의 __init__ 메소드가 호출되었습니다.")
        
child = Child()
child.test()
print(child.value)