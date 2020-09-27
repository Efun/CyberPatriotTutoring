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

#log in to the third account in the list

#remind me about linear search