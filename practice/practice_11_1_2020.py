import json

class player:
    #properties
    isImposter = False
    color = ""
    hat = None
    userName = ""

    #actions
    def __init__(self, userName, color):
        self.userName = str(userName)
        self.color = str(color)

    #getters and setters
    def getColor(self):
        return self.color

    def setColor(self, color):
        if (type(color) is str):
            self.color = color
        else:
            print("That's not a color!")

    def getIsImposter(self):
        return self.isImposter

    def setIsImposter(self, isImposter):
        if (type(isImposter) is bool):
            self.isImposter = isImposter
        else:
            print("That's not a boolean!")

    def getHat(self):
        return self.hat

    def setHat(self, hat):
        if (type(hat) is hatType):
            self.hat = hat
        else:
            print("no")

class Person:
    #properties
    name = ""
    age = 0

    #actions
    def __init__(self):
        self.name = "PersonClass"
        self.age = 21

#dicts - name value pairs
person = {
    "name": "PersonDict",
    "age": 21
}

person2 = {
    "name": "person2",
    "age": 22,
    "interalDict": {
        "random": "internalDictRandom"
    } 
}



var = Person()
#access in a class is done with .
print(var.name)

#access in a dict is done with []
print(person["name"])

#you can add things to the dict
person["gender"] = "female"

#this is bad practice but it works
var.gender = "female"

#remove things from the dict
person.pop("age")


# print(person)
# print(person2)

listOfDicts = []
listOfDicts.append(person)
listOfDicts.append(person2)

for x in listOfDicts:
    print(x)

#make a dict that replicates our player class in among us



playerDict = {
    "isImposter": False,
    "color": "Blue",
    "hat": None, 
    "userName": "test", 
}

playerJsonString = '{"isImposter": "False", "color": "Blue", "hat": "None", "userName": "test"}'
playerJsonToDict = json.loads(playerJsonString)

print("JSON")
print(playerJsonString)

print("Converted dict")
print(playerJsonToDict)

print("Our Dict")
print(playerDict)

print(str(playerDict["isImposter"] == playerJsonToDict["isImposter"]))

#json - java script object notation
#the reason for json and dicts is to pass information between people in a structured way
mineCraftPlayerDict = {
    "userName": ""
}

#aUPlayer = player(mineCraftPlayerDict["userName"])

#if i made a java object and i wanted to send it over to python
#i convert the java object into json
#json turns into a string
#python can consume that string and then convert it back to a dict/class
#provide a universal format for objects between any language

#things you can do with json/dicts


#serializing
#we convert from a python dict/object to json
convertPlayerFromDictToJson = json.dumps(playerDict)
print(convertPlayerFromDictToJson)

#in json, object type None -> null and Booleans convert to lower case


#deserializing
#we convert from json string to a python dict
print(json.loads(convertPlayerFromDictToJson))

#parsing
#we read a dict/json and convert it to an object
convertedPlayer = player(playerDict["userName"], playerDict["color"])
print(convertedPlayer.userName)
print(convertedPlayer.color)
convertedPlayer.setIsImposter(playerDict["isImposter"])
#convertedPlayer.setHat(playerDict["hat"])


#for next lesson
#think about the voting system
#(we may not get to) think about converting our player input to text and json