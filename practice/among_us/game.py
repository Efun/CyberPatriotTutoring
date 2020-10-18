from player import player

# player = player("a", "blue")
# print(player.userName + " " + player.color)



def isUserNameTaken(players, searchTerm):
    for x in players:
        #does the searchTerm match with x's username?
        if searchTerm == x.userName:
            #print("sorry this usernames taken")
            return True
    return False

def main():
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
            players.append(newPlayer)
    
    for x in players:
        print(x.userName + " " + x.color)

    #print out the user name and color of each player in the list

main()


