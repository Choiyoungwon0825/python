'''
class Car:                          # 클래스 Car 선언
    model ="BMW"                    # 멤버 변수
    color = "white"                 # 멤버 변수

    def speedChange(self,v):        # 메소드 정의
        print("speedChange")
        self.speed = v


# 객체 benz의 멤버 변수값 수정
benz.model = "Benz"
benz.color = "black"

print(bmw.model)
print(bmw.color)

print(benz.model)
print(benz.color)

class Car:
    # 멤버 변수
    count = 0
    speed = 0

    def speedChange(self, v):
        Car.count += 1              # 클래스 변수
        self.speed = v              # 인스턴스 변수


bmw = Car()                         # 객체 bmw 생성
benz = Car()                         # 객체 benz 생성

bmw.speedChange(100)                # 메소드 호출
print("bmw speed : ", bmw.speed)     # 인스턴스 변수 출력
print("number of speedChange : ", Car.count)     # 클래스 변수 출력

benz.speedChange(120)               # 메소드 호출
print("Benz speed : ", benz.speed)   # 인스턴스 변수 출력
print("number of speedChange : ", Car.count)  # 클래스 변수 출력
'''


class Car:  # 클래스 Car 선언
    # 생성자
    def __init__(self, model, color):
        self.model = model
        self.color = color

    # 차 정보 출력 메소드
    def info(self):
        print("Model: ", self.model, ", Color: ", self.color)


bmw = Car("BMW", "White")
benz = Car("Benz", "Black")

bmw.info()
benz.info()


class Person:
    name = "kai"

    def say():
        print("웰컴")


print(Person.say())


class Character:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def intro(self):
        print("Name : ", self.name)
        print("Weapon : ", self.weapon)


lugo = Character("Lugo", "gun")
lugo.intro()
print()


class TV:
    def __init__(self, ch, vol):
        self.power = True              # 켜져있음
        self.ch = ch
        self.vol = vol

    def onOff(self):
        if self.power:
            print("Turn on")
            self.power = False

        else:
            print("Turn off")
            self.power = True

        return self.power

    def info(self):
        print("---TV의 상태----")
        print("Power : {}".format(self.power))
        print("Channel : {}".format(self.ch))
        print("Volume : {}".format(self.vol))

    def setChannel(self, ch):
        if self.power:
            print("Channel : ", ch)
            return ch

    def setVolume(self, vol):
        print("Volume : ", vol)
        return vol


tv = TV(1, 16)
tv.info()
print("-------채널 변경-------")
tv.setChannel(5)
print("-------볼륨 변경-------")
tv.setVolume(12)
print("----------------------")
print(tv.onOff())
print("----------------------")
print(tv.onOff())
print("----------------------")
