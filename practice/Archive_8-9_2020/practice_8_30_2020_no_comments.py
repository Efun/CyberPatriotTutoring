#a sample function
def printHello():
    print("hello")
    print("lina")
    print("hanna")
    print("ethan")

#a sample function with params
def printHelloToPerson(name):
    print("hello")
    print(name)

#a sample function that returns something
def getUserInput():
    a = input("Please type in your name: ")
    return a

#a sample object
class animal:
    #properties - details
    size = 0
    age = 0

    #actions
    def __init__(self, size, age):
        self.size = int(size)
        self.age = int(age)

    def grow(self, growAmount):
        self.size += growAmount

    def getOlder(self):
        self.age += 1        

#set up the animal object: bobby
animalSize = input("What size is the animal: \n")
animalAge = input("What age is the animal?: \n")
bobby = animal(animalSize, animalAge)
print("The animal's size is " + str(bobby.size) + " inches")

#modify and print bobby's age
userInputGrowAmount = input("How much should the animal grow? \n")
bobby.grow(int(userInputGrowAmount))
print("Bobby's size is " + str(bobby.size) + " inches")
