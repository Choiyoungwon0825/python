class Character:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def intro(self):
        print(self.name,"(이) 가")
        print(self.weapon,"들고 협박함??")

class Action(Character):
    step = 0

    def moveForward(self, n):
        self.step += n
        print("Current Location is %d." % self.step)  # 앞으로 n 만큼 이동하는 메소드
        return n
    
    def moveBackword(self, n):
        self.step -= n
        print("Current Location is %d." % self.step) # 뒤로 n 만큼 이동하는 메소드
        return n
    
    def turnRight(self):
        print("Turn Right")                         # 오른쪽으로 회전하기
    
    def turnLeft(self):
        print("Turn Left")                          # 왼쪽으로 회전하기

lugo = Action("Lugo","gun")
lugo.intro()
lugo.moveForward(10)
lugo.moveBackword(3)
lugo.turnRight()
lugo.turnLeft()


