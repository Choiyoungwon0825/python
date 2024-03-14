class Student:
    # 생성자
    def __init__(self,name,korean,math,english,science):
        # self 클래스 내부의
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
            
    def getSum(self):
        return self.korean + self.math +self.english + self.science
    
    def getAvg(self):
        return self.getSum() / 4

    def toString(self):
        return "{}\t{}\t{}\t".format(
            self.name,
            self.getSum(),
            self.getAvg())

#학생 리스트 선언
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명원", 64, 88, 92, 92)
]

print("이름", "총점", "평균", sep='\t')

for student in students:
    #출력
    print(student.toString())
