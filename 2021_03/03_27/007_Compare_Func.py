# 크기 비교 함수

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
    
    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()
    
    
students = [
    Student("1", 87, 98, 88, 95),
    Student("2", 92, 98, 96, 98),
    Student("3", 76, 96, 96, 95),
    Student("4", 55, 66, 77, 88)
]


# 학생을 선언합니다.
student_a = Student("1", 87, 98, 88, 95),
student_b = Student("2", 92, 98, 96, 98),

print("student_a == student_b = ", student_a == student_b)
print("student_a != student_b = ", student_a != student_b)
print("student_a >  student_b = ", student_a > student_b)
print("student_a >= student_b = ", student_a >= student_b)
print("student_a <  student_b = ", student_a < student_b)
print("student_a <= student_b = ", student_a <= student_b)