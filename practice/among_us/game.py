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

    #         #we want the newPlayer's userName
    #         hatColor = input("What color does " + newPlayer.userName + " want your hat to be?" )
    #         hatStyle = input("What style does " + newPlayer.userName + " want your style to be? ")

    #         newHat = hat(hatColor, hatStyle)

    #         newPlayer.setHat(newHat)
    #         players.append(newPlayer)

    #write a for loop that makes 10 players with user name 0-9 and color blue

    #randint(start, stop) inclusive of start and stop
    #range(start, stop) inclusive of start but exclusive of stop

    for x in range(0, 3):
        userName = "user " + str(x) 
        color = "blue"
        hatColor = "blue"
        hatStyle = "birthday"
        newPlayer = player(userName, color)
        newHat = hat(hatColor, hatStyle)
        newPlayer.setHat(newHat)
        players.append(newPlayer)



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

def getVotes(players):
    #how should we ask each player for their vote?: we're going to ask 2 questions:
    #Do you want to vote?
    #if yes then cast your vote
    #if no then move on to the next player

    voteList = []
    
    for x in players: 
        askVote = input(x.userName + ", do you want to vote? \n") 
        if askVote == ("yes"):
            #then we get their vote
            
            votePlayer = input(x.userName + ", who do you want to vote for? \n")
            #then move on
        
            strTuple = (x.userName, votePlayer)
            voteList.append(strTuple)

    voteCountDict = {}

    #instead of doing this as tuples, change it to a dict instead.
    #start
    for x in players:
        #how do we make a key value pair of user name and value = 0
        # something["b"] = 12
        voteCountDict[x.userName] = 0

    for x in voteList:
        #@hanna how do we increment "user 0"'s value?

        #explain to me in english exactly what is happening on this line
        voteCountDict[x[1]] += 1
    #voteCountDict has {
    #   'userName': numVotes
    #   'userName2': numVotes
    # }
    print(voteCountDict)
    return voteCountDict



def main():
    #list of players
    players = getPlayers()

    getImposters(players)

    voteCountDict = getVotes(players)

    #how do we search voteCountDict for the maximum value?
    maximum = -1000000
    playerName = ""
    #right here is the first line
    for x in voteCountDict.items():
        if x[1] > maximum:
            maximum = x[1]
            playerName = x[0] 
            #right here is the second line
            
    print(playerName)

    #we need to save the x that contains the maximum number of votes so that we can use [0] to access the username
    #you need 2 lines of code to make this work


    [
        ('user 0', 0),
        ('user 1', 3),
        ('user 2', 0)
    ]

    #in the case of a tie, nothing happens
    #if nobody votes, nothing happens
    #we need to be able to handle a vote that is not in the list
    #we probably have to ask again
    #we need to have some way to keep track when iterating through our dict

    #we can either vote or not vote
    #whoever has the most votes gets kicked off
    
    
    for x in players:
        print(x.userName + " " + str(x.getIsImposter()))

    #find the max

    #we set some initial value that's really small
    #every time we find a value greater than it, we update that really small value to be that greater value instead
    
    

    

    
    


    
# strTuple = (string1, string2)

# tupList = []

# tupList.append(strTuple) 

    


main()
