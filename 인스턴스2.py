# isinstance(인스턴스, 클래스)

# 클래스 선언

class Student:
    count = 0
    def __init__(self,name,korean,math,english,science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

    def getSum(self):
        return self.korean + self.math + self.english + self.science
    
    def getAvg(self):
        return self.getSum() / 4
    
    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.getSum(),self.getAvg())
    
    def __eq__(self, value):
        return self.getSum() == value.getSum()
    def __ne__(self, value):
        return self.getSum() != value.getSum()
    def __gt__(self, value):
        return self.getSum() > value.getSum()
    def __ge__(self, value):
        return self.getSum() >= value.getSum()
    def __lt__(self, value):
        return self.getSum() < value.getSum()
    def __le__(self, value):
        return self.getSum() <= value.getSum()
    
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

student_a = Student("윤인성",87,98,88,95)
student_b = Student("연하진",92,98,96,98)

print("student_a == student_b = ",student_a == student_b)
print("student_a != student_b = ",student_a != student_b)
print("student_a > student_b = ",student_a > student_b)
print("student_a >= student_b = ",student_a >= student_b)
print("student_a < student_b = ",student_a < student_b)
print("student_a <= student_b = ",student_a <= student_b)

print()
print("현재 생성된 총 학생의 수는 {}명입니다.".format(Student.count))