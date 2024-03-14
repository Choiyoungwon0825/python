students = [
    {"name": "윤인성", "korean": 87, "math": 98, "english": 88, "sicence": 95},
    {"name": "연하진", "korean": 92, "math": 98, "english": 96, "sicence": 98},
    {"name": "구지연", "korean": 76, "math": 96, "english": 94, "sicence": 90},
    {"name": "나선주", "korean": 98, "math": 92, "english": 96, "sicence": 92},
    {"name": "윤아린", "korean": 95, "math": 98, "english": 98, "sicence": 98},
    {"name": "윤명원", "korean": 64, "math": 88, "english": 92, "sicence": 92}
]

# 학생을 한명씩 반복합니다
print("이름", "총점", "평균", sep="\t")
print("----------------")
for student in students:
    # 점수의 총합과 평균 ㅜㄱ하기
    scoreNum = student["korean"] + student["math"] + \
        student["english"]+student["sicence"]
    scoreAvg = scoreNum / 4
    print(student["name"], scoreNum, scoreAvg,sep="\t")

