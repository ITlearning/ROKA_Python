# 객체를 만드는 함수(1)
# 딕셔너리를 리턴하는 함수를 선언합니다.
def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

# 학생 리스트를 선언
students = [
    create_student("ITlearn", 87, 98, 97, 85),
    create_student("Kirri", 82, 83, 84, 85),
    create_student("Penguin", 95, 97, 96, 94),
    create_student("Lion", 86, 87, 94, 95)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_average = score_sum / 4
    print(student["name"], score_sum, score_average, sep="\t")