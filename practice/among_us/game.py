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
    keepGoing = "yes"
    
    while True:
        keepGoing = input("Do you want to add a new player? \n")

        if keepGoing != "yes":
            break

        userName = input("Type in your username \n")
        UserNameTaken = isUserNameTaken(players, userName)

        #what type is UserNameTaken?

        if UserNameTaken:
            print("sorry its taken")

        else:
            print("congratulations you created a new username!!11! \n")
            color = input("Which color would you like to be? ")
            newPlayer = player(userName, color)

            #we want the newPlayer's userName
            hatColor = input("What color does " + newPlayer.userName + " want your hat to be?" )
            hatStyle = input("What style does " + newPlayer.userName + " want your style to be? ")

            newHat = hat(hatColor, hatStyle)

            newPlayer.setHat(newHat)
            players.append(newPlayer)

    #write a for loop that makes 10 players with user name 0-9 and color blue

    #randint(start, stop) inclusive of start and stop
    #range(start, stop) inclusive of start but exclusive of stop

    # for x in range(0, 10):
    #     userName = str(x) 
    #     color = "blue"
    #     hatColor = "blue"
    #     hatStyle = "birthday"
    #     newPlayer = player(userName, color)
    #     newHat = hat(hatColor, hatStyle)
    #     newPlayer.setHat(newHat)
    #     players.append(newPlayer)



    return players
    
def getImposters(players):
    numImposters = input("How many imposters? \n")

    while not(1 <= int(numImposters) and int(numImposters) <= 3):
        print("Try again. That's not a valid number of imposters, there can be a min of 1 and a max of 3")

        numImposters = input("How many imposters? \n")
        #how do we ask them again until their input is correct?
        #we definitely want a loop

    if 1 <= int(numImposters) and int(numImposters) <= 3:
        print("cool!")
        print("We have " + numImposters + " imposters")

    #execute something a certain number of times == numImposters
    for x in range(0, int(numImposters)):
        #pick a random player from the list and then assign it to a variable
        
        #ask if the random player is already an imposter or not?
        randomNumber = random.randint(0, len(players) - 1)
        randomPlayer = players[randomNumber]
        
        #this is not a valid index, since this person is already an imposter
        while randomPlayer.getIsImposter() == True:
            randomNumber = random.randint(0, len(players) - 1)
            randomPlayer = players[randomNumber]

        #dicts json tomorrow
        
        #print(randomPlayer.userName)

        randomPlayer.setIsImposter(True)
        #print(str(randomPlayer.getIsImposter()))



def main():
    #list of players
    players = getPlayers()

    getImposters(players)

    #we can either vote or not vote
    #whoever has the most votes gets kicked off
    

    #how should we ask each player for their vote?: we're going to ask 2 questions:
    #Do you want to vote?
    #if yes then cast your vote
    #if no then move on to the next player
    
    voteList = []
    

    for x in players: 
        askVote = input(x.userName + ", do you want to vote?") 
        if askVote == ("yes"):
            #then we get their vote
            
            votePlayer = input(x.userName + "Who do you want to vote for?")
            #then move on
        
            strTuple = (x.userName, votePlayer)
            voteList.append(strTuple)

    #write a list and a variable for a tuple of user name and vote count

    #write a list of tuples of string and int
    string1 = "hello"
    number1 = 0
    strIntList = []

    strgiujiju = (string1, number1)
    strIntList.append(strgiujiju)

    #construct a bunch of tuples of each user name in the player list and the number 0
    voteCountList = []

    for x in players:
        string1 = x.userName
        count = 0

        strtuple = (string1, count) 
        voteCountList.append(strtuple) 


    for x in voteList:
        print(x)
    
    for x in players:
        print(x.userName + " " + str(x.getIsImposter()))
    
    

    

    
    


    
# strTuple = (string1, string2)

# tupList = []

# tupList.append(strTuple) 

    


main()
