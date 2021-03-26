# 딕셔너리로 객체 만들기
# 학생 리스트를 만듭니다.
students = [
    {"name": "ITlearn", "korean": 87, "math": 98, "english": 97, "science": 95 },
    {"name": "Kirri", "korean": 83, "math": 68, "english": 87, "science": 96 },
    {"name": "Penguin", "korean": 87, "math": 86, "english": 98, "science": 100 },
    {"name": "Lion", "korean": 86, "math": 96, "english": 96, "science": 95 }
]

# 학생을 한 명씩 반복합니다.
print("이름", "총점", "평균", sep="\t")

for student in students:
    # 점수의 종합과 평균을 구합니다.
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_average = score_sum / 4
    print(student["name"], score_sum, score_average, sep="\t")