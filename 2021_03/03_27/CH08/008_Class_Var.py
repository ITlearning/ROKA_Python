# 클래스 변수

class Student:
    count = 0
    
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        
        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))
        
students = [
    Student("1", 87, 98, 88, 95),
    Student("2", 92, 98, 96, 98),
    Student("3", 76, 96, 96, 95),
    Student("4", 55, 66, 77, 88)
]

print()
print("현재 생성된 총 학생의 수는 {}명입니다.".format(Student.count))

# 클래스 내부와 외부에서 클래스 변수에 접근할 때는 모두 Student.count 형태 (클래스이름.변수이름)를 사용합니다.