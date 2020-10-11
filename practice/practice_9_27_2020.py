from classes.BankAccount import BankAccount

# test = BankAccount('a', 'a', 100)
# print(test.balance)

# write a list of 5 elements containing tennis player names
tennisPlayers = ["serena williams", "roger federer", "rafael nadal", "novak djokovic", "rod laver"]


#print the second element of this list
#print (tennisPlayers[1])


#loops
#for loop will loop through an list like this:
#for varName in listName:

#for each tennis player in the list named tennisPlayers

idx = 0
for tennisPlayer in tennisPlayers:
    #print(str(idx) + ".) " + tennisPlayer)
    idx += 1

#for loop through numbers
#for varName in range(number)
#i will start at 0
# for x in range(5):
#     print(str(x) + ".) " + "hi")


#range(initial_val, max_val, step_size)
#x is set to the initial_val, and then increases by step size until it exceeds the max_val
# for x in range(5, 10, 2):
#     print(str(x) + ".) " + "hi")

#print out all tennis players using range instead of in tennisPlayers
#set the variable to be the place in the list where the tennis player is

#how do we get all of the numbers we need?
#x = 0, 1, 2, 3, 4
#tennisPlayers[x]
for x in range(0, 5, 1):
    #print(tennisPlayers[x])

#print out every other tennis player starting at serena williams

for x in range(0, 5, 2):
    #print(tennisPlayers[x])

#for x in range(5) == for x in range(0, 5, 1)

tennisPlayerA = "Lina"
tennisPlayers.append(tennisPlayerA)

#print(tennisPlayers[5])


userName = input("Type in your username.")
password = input("Type in your passwrord.")
balance = 100

bankAccounts = []


newBankAccount = BankAccount(userName, password, balance)
bankAccounts.append(newBankAccount)


