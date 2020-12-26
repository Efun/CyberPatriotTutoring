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
        #put something here to make sure that we don't ask dead players to vote.
        #if *** 
        #it's an if statement! (what's our condition for the if statement?)
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

def maximumValue(voteCountDict): 
    maximum = -1000000
    maximumPlayerName = ""
    #right here is the first line
    for x in voteCountDict.items():
        if x[1] > maximum:
            maximum = x[1]
            maximumPlayerName = x[0] 
            #right here is the second line
    
    #return None if there is a tie
    #return the maximumPlayerName if there is not a tie
    if tie(voteCountDict, maximum, maximumPlayerName):
        return None 
    else: 
        return(maximumPlayerName)

#question here is was there a tie or not?
#return True
#return False
def tie(voteCountDict, maximum, maximumPlayerName):
    for x in voteCountDict.items(): 
        if maximum == x[1]: 
            #we want to check that the current x's fruit name is not equal to the max fruit before we print
            if x[0] != maximumPlayerName:
                print("It's a tie")
                return (True)
    return (False)

def hitlist(players): 
    #loop through all of the players to see who is an imposter
    for x in players:
        if x.getIsImposter():
            #our output right now: 
            #   user 0 Is imposter: true/false Is alive: true/false
            #   1.) user 0 Is imposter: t/f Is alive: t/f 
            #also there's a bug in this for loop, what is it?
            print(x.userName + " you are an imposter: ")
            
            integerVariable = 1

            for y in players:
                print(str(integerVariable) + ". " + y.userName + " " + "Is imposter: " + str(y.getIsImposter()) + " Is alive: " + str(y.isAlive))
                integerVariable += 1
    
            playerToKill = input("Who do you want to kill? ")
            players[int(playerToKill) - 1].murder()

def voteOut(players, votedOutPlayer): 
    print(votedOutPlayer)
    for x in players:
        if x.userName == votedOutPlayer: 
            x.murder()

def main():
    #list of players
    players = getPlayers()

    getImposters(players)
    #how do we search voteCountDict for the maximum value?
   
    #we're trying to find the player whose username is equal to voted out player (and kill them)
    


    #getIsImposter()
    #input statement to ask these people a question\
    #save that as a variable
    #we just run the murder() command


    hitlist(players)
    
    voteCountDict = getVotes(players)

    votedOutPlayer = maximumValue(voteCountDict)

    voteOut(players, votedOutPlayer)
    
    for x in players:
        print(x.userName + " " + str(x.getIsImposter()) + " alive: " + str(x.isAlive))

    #find the max

    #we set some initial value that's really small
    #every time we find a value greater than it, we update that really small value to be that greater value instead
    
    

    
    


    
# strTuple = (string1, string2)

# tupList = []

# tupList.append(strTuple) 

    


main()
