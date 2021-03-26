def create_strdent(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

# 학생을 처리하는 함수를 선언합니다.
def student_get_sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]

def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(student["name"], student_get_sum(student), student_get_average(student))

# 학생 리스트를 선언합니다.

students = [
    create_strdent("1", 45, 65, 45, 78),
    create_strdent("2", 98, 98, 97, 94),
    create_strdent("3", 85, 94, 97, 64),
    create_strdent("4", 45, 87, 88, 98)
]

# 학생을 한 명씩 반복합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))