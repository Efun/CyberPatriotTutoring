#Linear Search Practice

def fruitSearch():
    fruitsList = ["apple", "banana", "orange", "kiwi", "watermelon", "pineapple"]

    userInput = input("Which fruit do you want to find?")

    notFound = True
    #how do we know if something is not found?

    for x in fruitsList:
        if userInput == x:
            print("There is a " + userInput + " in the list")
            notFound = False
            break #ends the loop early

    if notFound == True: 
        print("There is no " + userInput + " in the list")

    

def animalSearch():
    animalsList = ["dog", "cat", "rat"]
    
    userInput = input("Which animal do you want to find?")

    notFound = True

    for x in animalsList:
        if userInput == x:
            print("There is a " + userInput + " in the list")
            notFound = False
            break
    if notFound == True:
        print("There is no " + userInput + " in the list")


fruitSearch()
animalSearch()
