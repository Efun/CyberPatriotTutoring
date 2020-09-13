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


#make account
#ask user to log in
#ask user how much money to deposit

def main():
    #get userInput to make a new bank account
    #make a new bank account with your name and a password
    ba = BankAccount("Ethan", "123", 1000000)

    #update withdraw and deposit so that not everybody can do that 
    #HINT: if statements

    #use user input to do these things
    #log in to your account and deposit x dollars 
    #ask for a password

    #log out of your account
    ba.logout()

main()