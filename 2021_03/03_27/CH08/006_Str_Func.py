# __str__() 함수

# 클래스를 선언합니다.
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )
    
    
# 학생 리스트를 선언합니다.
students = [
    Student("1", 87, 98, 88, 95),
    Student("2", 92, 98, 96, 98),
    Student("3", 76, 96, 96, 95),
    Student("4", 55, 66, 77, 88)
]


# 츌력합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(str(student)) # str 함수의 매개변수로 넣으면 student의 __str__() 함수가 호출됩니다.