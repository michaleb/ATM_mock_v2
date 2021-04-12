import random
from datetime import datetime

#database = {} # Dictionary of user credentials

def login():
    
    accNum = int(input("\nPlease enter your account number "))
    for account in database.keys():
        if accNum == account:
            passwdAttempts = 0
            while passwdAttempts < 3:
                userPassword = input("Please enter your password ")
                if database[account][3] == userPassword:
                    passwdAttempts = 3
                    print("\nWelcome! %s %s" %(database[account][0], database[account][1]))
                    bankOperations(account)
                else:    
                    print("Incorrect password. Please try again \n")
                    passwdAttempts += 1
            login()
        
    print("Invalid account number. Please try again \n")
    init()

    return         


def register():

    print("*******User registration******* \n")
    first_name = input("Please enter your first name ") 
    last_name = input("Please enter your last name ")
    email = input("Please enter your email address ")
    password = input("Please create your password ")
    acc_balance = 0

    accountNum = genAccNum()
    database[accountNum] = [first_name, last_name, email, password, acc_balance]
    print("=======================================")
    print("| Your account number is : %d |" %accountNum)
    print("=======================================")

    login()

    return


def updateBalance(availableBalance, request):
    availableBalance += request
    return availableBalance
    

def bankOperations(accountNum):
    
    print("\n These are the available options:\n")
    print("1. Withdrawal")
    print("2. Cash Deposit")
    print("3. Exit")

    accountBalance = database[accountNum][4]
    selectedOption = input("\n Please select a number option: ")
    if (selectedOption == "1"):
        
        print("You selected option %s" %selectedOption)
        amount = int(input("How much would you like to withdraw: "))
        print("Please wait system processing... \n")

        if (amount <= accountBalance):
            amount *= -1
            database[accountNum][4] = updateBalance(accountBalance, amount)
            
            print("Please take your cash...")
            print("Your current balance is $ %s" %database[accountNum][4])
            bankOperations(accountNum)
        else:
            print("Amount not available, Insufficient funds")
            print("Please try again")
            bankOperations(accountNum)
    
    elif (selectedOption == "2"):
        
        print("You selected option %s" %selectedOption)
        amount = int(input("Please enter your deposit amount: "))
        print("Please wait processing... \n")
        database[accountNum][4] = updateBalance(accountBalance, amount)
        print("Your current  balance is $ %s" %database[accountNum][4])
        bankOperations(accountNum)
    
    elif (selectedOption == "3"):
        
        print("You selected option %s \n" %selectedOption)
        print("Thank you for banking with us. Good bye!")
        init()
    
    else: 
        print("Invalid option, please try again \n") 
        bankOperations(accountNum)

    return

def genAccNum():
    validAccNum =  random.randrange(111111111, 999999999)
    if (validAccNum % 11 != 0):
        genAccNum() 
    else:
        return validAccNum
           

def init():
    
    print(datetime.now().strftime("%m/%d/%Y - %H:%M:%S \n"))
    print("Welcome! to BankONE ATM \n") 
    
    accountOption = input("\nDo you have an account with us? (1 for yes, 2 for no)? ")
    if accountOption == "1":
        login()
    elif accountOption == "2":
        register()   
    else:
        print("Invalid option entered, Please try again") 
        init()    
    
    return
            

if __name__ == "__main__":
    init()