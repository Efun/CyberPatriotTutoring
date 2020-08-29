# #if statement

# #boolean
# hasCough = False
# hasDifficultyBreathing = False
# hasFever = False
# hasInternationalTravel = False
# shouldQuarantine = False

# #magic scanner, that can detect covid
# def scanner():
#   scan(person)
  
# def scan(p):
#   #pretend that this function sets all of the values correctly


# # def main():
# #   lina = person("Lina") #lina is a person
# #   #person with the name Lina
# #   print(lina.name)
# #   #what would i print here?
# #   #Lina
# #   scan(lina)


# p = person("Hanna", "5'3 and a half", "brown", "brown")
# print(p.name)
# #Hanna
# print(p.height)
# #5'3 and a half

# def printName():
#     p = person("Hanna", "5'3 and a half", "brown", "brown")
    
#     print("hello")
#     print(p.name)

def printName2(person):
    print("hello")
    print(person.name)

class person:
    #properties
    name = ""
    height = ""
    eyeColor = ""
    hairColor = ""

    #actions
    #set up the person
    def __init__(self, name, height, eyeColor, hairColor): #i'm creating a person
        self.name = name #sets our object's name = "Hanna"
        self.height = height #sets our objec'ts height = "5'3 and a half"
        self.eyeColor = eyeColor 
        self.haircolor = hairColor

p1 = person("Hanna", "5'3 and a half", "brown", "brown")
p2 = person("Lina", "3'5", "brown", "black")

printName2(p2)
printName2(p1)
