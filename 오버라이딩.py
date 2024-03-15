class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        print("Model : ,", self.model, "Color", self.color)

# 클래스 CarDrive(Car):


class CarDrive(Car):
    # info() 메소드 오버라이딩
    def info(self):
        print("The model of this is car is %s." % self.model)
        print("The color is %s." % self.color)

    def speedChange(self, v):
        self.speed = v
        print("speedChange: ", self.speed)


bmw = CarDrive("BMW", "White")
bmw.info()
bmw.speedChange(100)

class Parent:
    def info(self):
        print("Parent Class")

class ChildA(Parent):
    def info(self):
        super().info()  # 부모 클래스의 info() 메서드 호출
        print("A Child Class")

aChild = ChildA()
#  # 자식 클래ㅔ스에서 재정의된 info()
aChild.info()
Parent.info(aChild)

class Character:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def intro(self):
        print(self.name,"(이) 가")
        print(self.weapon,"들고 협박함??")

lugo = Character("Lugo","gun")
lugo.intro()