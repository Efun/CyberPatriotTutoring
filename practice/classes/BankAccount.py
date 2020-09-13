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