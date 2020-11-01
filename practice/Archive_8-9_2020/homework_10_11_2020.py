
#modify last week's homework:
#package linear search as a function
#use this function to solve the problem of having multiple of the same username
#This linear search should be applicable to any list of bank accounts


# import the bank account class
class BankAccount:
    # properties
    userName = ""
    password = ""
    balance = 0.0
    isLoggedIn = False

    # actions
    def __init__(self, userName, password, balance):
        self.userName = userName
        self.password = password
        self.balance = balance

    # withdraw
    def withdraw(self, withdrawAmt):
        if self.isLoggedIn == True:
            self.balance -= withdrawAmt

    # deposit
    def deposit(self, depositAmt):
        if self.isLoggedIn == True:
            self.balance += depositAmt

    # getBalance
    def getBalance(self):
        return self.balance

    # login
    def login(self, password):
        # is the password that you gave me the same as the password for this account?
        if password == self.password:
            self.isLoggedIn = True

    # logout
    def logout(self):
        self.isLoggedIn = False

#this function returns true if we found a user name in the list and false if we did not find the user name in the list
def isUserNameTaken(bankAccountList, searchTerm):
    for x in bankAccountList:
        #does the searchTerm match with x's username?
        if searchTerm == x.userName:
            #print("sorry this usernames taken")
            return True
    return False






# create user input to add 3 bank accounts to a list
bankAccountList = []

#we can do an infinite amount of usernames, the user needs to input when to stop
keepGoing = "yes"

# append function
while True:
    keepGoing = input("Do you want to create a new bank account? \n")

    if keepGoing != "yes":
        break

    userName = input("Type in your username \n")
    

    #this will equal true or false based on our function's logic
    #recalls function line 47 
    
    UserNameTaken = isUserNameTaken(bankAccountList, userName)

    #what type is UserNameTaken?

    if UserNameTaken:
        print("sorry its taken")

    else: 
        print("congratulations you created a new username!!11! \n")
        password = input("Type in your password \n")
        balance = input("How much money do you have \n")
        newBankAccount = BankAccount(userName, password, balance)
        bankAccountList.append(newBankAccount)


    #if the username is taken, print out sorry this username is taken

 


# for x in bankAccountList:
#     print(str(x.userName))

# log in to the third account in the list

requestBankAccountUserName = input("Which bank account do you want to log into? \n")


numBankAccount = len(bankAccountList)
iterations = 0
for x in bankAccountList:
    # x = bankAccountList[0]
    # x = bankAccountList[1]...
    
    if requestBankAccountUserName == x.userName:
        tries = 3
        
        while tries > 0:
            password = input("Type the password for account " + str(x.userName))
            x.login(password)
            if x.isLoggedIn == True:
                print("Success!")
                break
            elif x.isLoggedIn == False and requestBankAccountUserName == x.userName:
                tries -= 1
                print("Failure, try again you have " + str(tries) + " more tries left. \n") # with this print statement, also print out how many tries we have left

        #if we did not log in successfully
        if x.isLoggedIn == False:
            print("bye cy@")
            break

    if iterations == numBankAccount - 1 and (x.isLoggedIn == False):
        print("We couldn't find the account")

    iterations += 1

#we should have a certain number of attempts and say how many are remaining before exiting the program

#number of tries?

# for an action we need parentheses and parameters
# for a property we only need the property name

# remind me about linear search


#what if we have input of two user names being the same?