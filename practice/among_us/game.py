from player import player
from hat import hat
import random

# player = player("a", "blue")
# print(player.userName + " " + player.color)


def isUserNameTaken(players, searchTerm):
    for x in players:
        #does the searchTerm match with x's username?
        if searchTerm == x.userName:
            #print("sorry this usernames taken")
            return True
    return False

#move the user input player loop into a function/method
#write a function called getPlayers


def getPlayers():
    players = []


    # keepGoing = "yes"
    
    # while True:
    #     keepGoing = input("Do you want to add a new player? \n")

    #     if keepGoing != "yes":
    #         break

    #     userName = input("Type in your username \n")
    #     UserNameTaken = isUserNameTaken(players, userName)

    #     #what type is UserNameTaken?

    #     if UserNameTaken:
    #         print("sorry its taken")

    #     else:
    #         print("congratulations you created a new username!!11! \n")
    #         color = input("Which color would you like to be? ")
    #         newPlayer = player(userName, color)
    #         hatColor = input("What color does" + x.userName + "want your hat to be?" )
    #         hatStyle = input("What style does" + x.userName + "want your style to be? ")

    #         newHat = hat(hatColor, hatStyle)

    #         newPlayer.setHat(newHat)
    #         players.append(newPlayer)

    #write a for loop that makes 10 players with user name 0-9 and color blue

    #randint(start, stop) inclusive of start and stop
    #range(start, stop) inclusive of start but exclusive of stop

    for x in range(0, 10):
        userName = str(x) 
        color = "blue"
        hatColor = "blue"
        hatStyle = "birthday"
        newPlayer = player(userName, color)
        newHat = hat(hatColor, hatStyle)
        newPlayer.setHat(newHat)
        players.append(newPlayer)



    return players
    



def main():
    #list of players
    players = getPlayers()

    # for x in players:
    #     print(x.userName + " " + x.color + "\nhat: " +
    #           x.getHat().color + " " + x.getHat().style)


    #we can have a max of 3 a min of 1 imposter
    #get user input for the numnber of imposto/ers
    # 1 <= numImposters <= 3

    #find what's missing here
    #you need 1 line of code to make this correct
    #make sure that the number of imposters is between 1 and 3 (inclusive)
    #it should be above the while loop

    while !(1 <= int(numImposters) and int(numImposters) <= 3):
        print("Try again. That's not a valid number of imposters, there can be a min of 1 and a max of 3")

        numImposters = input("How many imposters? \n")
    
        
   
        #how do we ask them again until their input is correct?
        #we definitely want a loop

    if 1 <= int(numImposters) and int(numImposters) <= 3:
        print("cool!")
    
    #pick a random player from the list and then assign it to a variable
    randomNumber = random.randint(0, len(players) - 1)
    randomPlayer = players[randomNumber]
    print(randomPlayer.userName)

    randomPlayer.setIsImposter(True)
    print(str(randomPlayer.getIsImposter()))
    


main()
