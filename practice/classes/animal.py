#a sample object
class animal:
    #properties - details
    size = 0
    age = 0
    color = ""
    gender = ""
    breed = ""

    #actions
    def __init__(self, size, age, color, gender, breed):
        self.size = int(size)
        self.age = int(age)
        self.color = str(color)
        self.gender = str(gender)
        self.breed = str(breed)

    def grow(self, growAmount):
        self.size += growAmount

    def getOlder(self):
        self.age += 1  

    def dyeAnimal(self, color):
        self.color = str(color)