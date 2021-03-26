# 클래스 내부에 함수(메소드) 선언하기
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

    def to_string(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average())
    
students = [
    Student("1", 45, 65, 45, 78),
    Student("2", 46, 78, 87, 97),
    Student("3", 46, 78, 76, 97),
    Student("4", 87, 78, 87, 97),
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_string())