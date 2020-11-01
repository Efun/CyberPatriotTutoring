#import the bank account class
class BankAccount:
    #properties
    userName = ""
    password = ""
    balance = 0.0
    isLoggedIn = False

    #actions
    def __init__(self, userName, password, balance):
        self.userName = userName
        self.password = password
        self.balance = balance

    #withdraw
    def withdraw(self, withdrawAmt):
        self.balance -= withdrawAmt

    #deposit
    def deposit(self, depositAmt):
        self.balance += depositAmt

    #getBalance
    def getBalance(self):
        return self.balance

    #login
    def login(self, password):
        #is the password that you gave me the same as the password for this account?
        if password == self.password:
            self.isLoggedIn = True

    #logout
    def logout(self):
        self.isLoggedIn = False

#create user input to add 3 bank accounts to a list
bankAccountList = []

#append function
for x in range(0, 3):
    userName = input("Type in your username \n")
    password = input("Type in your password \n") 
    balance = input("How much money do you have \n")

    newBankAccount = BankAccount(userName, password, balance)
    bankAccountList.append(newBankAccount)

# for x in bankAccountList:
#     print(str(x.userName))

#log in to the third account in the list
curBankAccount = (bankAccountList[2])
password = input("Type the password for account " + str(curBankAccount.userName))
curBankAccount.login(password)

if curBankAccount.isLoggedIn == True:
    print("Success!")
else:
    print("Failure")


#for an action we need parentheses and parameters
#for a property we only need the property name


#remind me about linear search