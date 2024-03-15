#모듈가져오기
import math

# 클래스 선언
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getCircumference(self):
        return 2 * math.pi * self.radius
    
    def getArea(self):
        return math.pi * (self.radius**2)
    
circle = Circle(10)
print("원 넓이", circle.getCircumference())
print("원 둘레", circle.getArea())