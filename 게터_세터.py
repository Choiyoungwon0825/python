
import math

# 클래스 선언


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def getCircumference(self):
        return 2 * math.pi * self.__radius

    def getArea(self):
        return math.pi * (self.__radius**2)

    def getRadius(self):
        return self.__radius

    def setRadius(self, value):
        self.__radius = value


circle = Circle(10)
print("원 넓이", circle.getCircumference())
print("원 둘레", circle.getArea())
print()

print(".__radius에 접근")
print(circle.getRadius())
print()

circle.setRadius(2)
print("# 반지름 변경하고 원의 둘레 넓이 구하기")
print("원 넓이", circle.getCircumference())
print("원 둘레", circle.getArea())
