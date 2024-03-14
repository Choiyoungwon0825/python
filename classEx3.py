def createStudent(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

# 점수를 처리하는 함수


def studentGetSum(student):
 return student["korean"]+student["math"] +\
     student["english"]+student["science"]


def studentGetAvg(student):
   return studentGetSum(student) / 4


def studentToString(student):
   return "{}\t{}\t{}\t".format(
       student["name"],
       studentGetSum(student),
       studentGetAvg(student))


students = [
    createStudent("윤인성", 87, 98, 88, 95),
    createStudent("연하진", 92, 98, 96, 98),
    createStudent("구지연", 76, 96, 94, 90),
    createStudent("나선주", 98, 92, 96, 92),
    createStudent("윤아린", 95, 98, 98, 98),
    createStudent("윤명원", 64, 88, 92, 92)
]


print("이름", "총점", "평균", sep='\t')

for student in students:
   #출력
   print(studentToString(student))
   