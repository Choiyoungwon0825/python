# 모듈 가져옴
import math

#클래스 선언
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
    
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자여야 합니다.")
        self.__radius = value
        
print("# 데코레이터를 사용한 Getter 와 Setter")
circle = Circle(10)
print("원래 원 반지름: ",circle.radius)
circle.radius = 2
print("변경된 원의 반지름: ", circle.radius)
print()

print("# 강제 예외 발생")
circle.radius = -10