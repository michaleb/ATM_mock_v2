import os
import random
import database, helper
from getpass import getpass
from datetime import datetime


timestamp = datetime.now().strftime("%m/%d/%Y - %H:%M:%S \n")
user_auth_path = "data/auth_session/"

def login():
    
    accNum = input("\nPlease enter your account number ")
    valid_account_number = helper.account_number_validation(accNum)

    if valid_account_number:
        user_acc_on_record = helper.account_number_exist(accNum)
        if user_acc_on_record:
            passwdAttempts = 0
            while passwdAttempts < 3:
                userPassword = getpass("Please enter your password ")
                user = helper.authenticated_user(accNum, userPassword)
                
                if user:
                    passwdAttempts = 3
                    print("\nWelcome! %s %s" %(user[0], user[1]))
                    
                    # create login timestamp  file in auth_session folder
                    f = open(user_auth_path + str(accNum) + ".txt", "w")
                    f.write("Customer" + " " + user[0] + " " + user[1] + " " + "logged in at" + " " + timestamp)
                    f.close()

                    bankOperations(accNum)
                else:    
                    print("Incorrect password. Please try again \n")
                    passwdAttempts += 1
            login()
        
    print("Invalid account number. Returning user to Welcome screen \n")
    init()

    

def register():

    print("*******User registration******* \n")
    first_name = input("Please enter your first name ") 
    last_name = input("Please enter your last name ")
    email = input("Please enter your email address ")
    password = input("Please create your password ")
    acc_balance = 0

    accountNum = genAccNum()
    is_user_created = database.create(accountNum, first_name, last_name, email, password, acc_balance)

    if is_user_created:

        print("=======================================")
        print("| Your account number is : %d |" %accountNum)
        print("======================================= \n")

        login()

    else:
        print("Internal error!, Please try again")
        register()
 

def updateBalance(availableBalance, request):
    availableBalance += request
    return availableBalance
    

def get_current_balance(acc):
    return int(str.split(database.read(acc), ',')[4])


def bankOperations(accountNum):
    
    print("\n These are the available options:\n")
    print("1. Withdrawal")
    print("2. Cash Deposit")
    print("3. Check Balance")
    print("4. Log Out")
    print("5. Exit")

    accountBalance = get_current_balance(accountNum)
    selectedOption = input("\n Please select a number option: ")
    
    if (selectedOption == "1"):
        
        print("You selected option %s" %selectedOption)
        amount = input("How much would you like to withdraw: ")

        is_input_valid = helper.input_validation(amount)
        
        if is_input_valid:
            amount = int(amount)
            print("Please wait system processing... \n")

            if (amount <= accountBalance):
                amount *= -1
                current_balance = updateBalance(accountBalance, amount)
                database.update(accountNum, current_balance)
                
                print("Please take your cash...")
                print("Your current balance is $ %s" %get_current_balance(accountNum))
                bankOperations(accountNum)
            else:
                print("Amount not available, Insufficient funds")
                print("Please try again")
                bankOperations(accountNum)

        else: 
            print("\nInvalid amount entered, please try again \n")  
            bankOperations(accountNum)          
    
    elif (selectedOption == "2"):
        
        print("You selected option %s" %selectedOption)
        amount = input("Please enter your deposit amount: ")

        is_input_valid = helper.input_validation(amount)
        
        if is_input_valid:
            amount = int(amount)
            print("Please wait processing... \n")
            current_balance = updateBalance(accountBalance, amount)
            database.update(accountNum, current_balance)
            print("Your current  balance is $ %s" %get_current_balance(accountNum))
            bankOperations(accountNum)

        else: 
            print("\nInvalid amount entered, please try again \n")  
            bankOperations(accountNum)  
    
    elif (selectedOption == "3"):

        print("You selected option %s \n" %selectedOption)
        print("Your current balance is $ %s" %get_current_balance(accountNum))
        bankOperations(accountNum)    
    
    elif (selectedOption == "4"):
        
        print("You selected option %s \n" %selectedOption)
        print("You are now logged out of the system")
        
        # delete login timestamp file from auth_sessions folder
        os.remove(user_auth_path + str(accountNum) + ".txt")

        login()
    
    elif (selectedOption == "5"):
        
        print("Thank you for banking with us. Good bye!")

        if ((user_auth_path + str(accountNum) + ".txt")):
            os.remove(user_auth_path + str(accountNum) + ".txt")
        exit()
           
    else: 
        print("Invalid option, please try again \n") 
        bankOperations(accountNum)

    

def genAccNum():
    return  random.randrange(1111111111, 9999999999) 
    

def init():
    
    print(timestamp)
    print("Welcome! to BankONE ATM \n") 
    
    accountOption = input("\nDo you have an account with us? (1 for yes, 2 for no)? ")
    if accountOption == "1":
        login()
    elif accountOption == "2":
        register()   
    else:
        print("Invalid option entered, Please try again") 
        init()    
    
              
if __name__ == "__main__":
    init()
