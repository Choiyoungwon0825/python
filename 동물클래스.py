class Animal:
    def __init__(self, species):
        self.species = species

    def move(self):
        print("움직입니다.")

class Fish:
    def __init__(self, scale_color):
        self.scale_color = scale_color

    def swim(self):
        print("수영합니다.")

class Bird:
    def __init__(self, feather_color) :
        self.feather_color = feather_color

    def fly(self):
        print("날아갑니다.")

class FishBird(Animal, Fish, Bird):
    def __init__(self, species, scale_color, feather_color):
        Animal.__init__(self, species)
        Fish.__init__(self, scale_color)
        Bird.__init__(self,feather_color)

fish_bird = FishBird("Fugu","Silver","Blue")
print("종 : ",fish_bird.species)
print("비늘 색 : ", fish_bird.scale_color)
print("털 색 : ",fish_bird.feather_color)
fish_bird.move()
fish_bird.swim()
fish_bird.fly()

