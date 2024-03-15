class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color 
    def info(self):
        print("Model : ,",self.model , "Color" , self.color)

# 클래스 CarDrive(Car):
class CarDrive(Car):
    def speedChange(self, v):
        self.speed = v
        print("speedChange: ", self.speed)
        
bmw = CarDrive("BMW","White")
bmw.info()
bmw.speedChange(100)

