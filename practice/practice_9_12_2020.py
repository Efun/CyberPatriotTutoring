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

#set up the animal object: bobby
animalSize = input("What size is the animal: \n")
animalAge = input("What age is the animal?: \n")
animalColor = input("What color is the animal?: \n")
animalGender = input("What gender is the animal?: \n")
animalBreed = input("What breed is the animal?: \n")
bobby = animal(animalSize, animalAge, animalColor, animalGender, animalBreed)
print("The animal's size is " + str(bobby.size) + " inches")

#modify and print bobby's age
userInputGrowAmount = input("How much should the animal grow? \n")
bobby.grow(int(userInputGrowAmount))
print("Bobby's size is " + str(bobby.size) + " inches")

#get input for what color to dye the animal
colorDye = input("What color do you want to dye it? \n")
bobby.dyeAnimal(colorDye)


joe = animal(420, 69, blue, "girl", "cat")

#boolean
#if the cat is bigger than 100 inches it's pretty big

#if the cat is really big, we're going to say "ok"
#joe's size = joe.size
#bobby's size = bobby.size
if joe.size >= 100: 
  #result
  print("ok")

joe.getOlder()

#if joe is really old, we're going to say: "wow (s)he's so old"
if joe.age >= 70:
  x = "do nothing"
  print("wow he's so old!")
  print("when was the last time you ate lunch")
