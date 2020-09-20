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
    
  AskAccount = input("Do you have a login? \n")

  if AskAccount == "yes": 
    AskUserName = input("What is your username?")
    AskPassword = input("What is your password?")

    if AskPassword == ba.password and AskUserName == ba.userName: 
            # balance = 0

      amountadded = int(input("How much money do you want to deposit into your account? "))

            # balance+=amountadded

      ba.deposit(amountadded)

      print("You have now have")
      print(ba.balance) 
      print("$ in your account")
    
    else: 
      print("Wrong password.")
             
  else: 
    userName = input("Create your username: ")
    password = input("Create your password: ")

    newba = BankAccount(userName, password, 0)
    print(newba.userName + newba.password)



main()