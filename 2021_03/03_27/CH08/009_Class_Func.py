# 클래스 함수

class Student:
    count = 0
    students = []
    
    @classmethod
    def print(cls):
        print("-------- 학생 목록 --------")
        print("이름", "총점", "평균", sep="\t")
        for student in cls.students:
            print(str(student))
        print("------ ------ ------ ------")
        
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)
    
    
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
    
    
Student("1", 87, 98, 88, 95)
Student("2", 92, 98, 96, 98)
Student("3", 76, 96, 96, 95)
Student("4", 55, 66, 77, 88)

Student.print()