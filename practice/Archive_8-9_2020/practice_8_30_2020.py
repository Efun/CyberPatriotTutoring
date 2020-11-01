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
    #instead of __init__("12"), animal("12")
    #size = whatever you put inside the parentheses
    def __init__(self, size, age): #animal("whatever size")
        self.size = int(size)
        self.age = int(age)

    #we want the animal to get bigger
    #how much do we want the animal to grow?
    def grow(self, growAmount):
        self.size += growAmount
        #add growAmout to my size

    def getOlder(self):
        self.age += 1        

# integer, boolean, string, animal
# animal1 = animal()
# animalSize = animal1.size

# print(animalSize)

# personName = getUserInput()
# printHelloToPerson(personName)

x = 0
#x is a variable of type integer with value 0

#ask a user what size of animal they want to create
#\n == enter key
animalSize = input("What size is the animal: \n")
animalAge = input("What age is the animal?: \n")
bobby = animal(animalSize, animalAge)
#bobby is a variable of type animal
#bobby is an animal, and his size is animalSize
#call __init__(animalSize)


#i want the bobby's size
#'s == .
print("The animal's size is " + str(bobby.size) + " inches")

#i want my animal to grow by user input inches
userInputGrowAmount = input("How much should the animal grow? \n")

#bobby, please grow by user input inches

bobby.grow(int(userInputGrowAmount))
#
print("Bobby's size is " + str(bobby.size) + " inches")
