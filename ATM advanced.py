#register
# - first name, last name, password, email
# - generaten user account


#login
# - account number & password


#bank operations

#Initializing the system
import random

database = {} #dictionary

def ask():
    print("Welcome to Church Bank")
    action = int(input("Press: (1)Login (2)Register (3)exit \n"))
    init(action)

def init(action):

    if(action == 1):
        login()

    elif(action == 2):
        register()

    elif(action == 3):
        print('\n ##### Thank you for using Church Bank, Do have a nice day ###')
    

    else:
        print("You have selected invalid option")
        action = int(input("Press: (1)Login (2)Register (3)exit \n"))
        init(action)


def login():
    
    print("********* Login ***********")

    user_acct_number = int(input("What is your account number? \n"))
    user_password = input("What is your password \n")

    for accountNumber, password in database.items():
        if(accountNumber == user_acct_number):
            if(password[3] == user_password):
                bankOperation(password)
                anotherTraction()
        else:
           print('Invalid account or password')
           login()

    


def register():

    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()

def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )

    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Customer Service (4) Logout (5) Exit \n"))

    if(selectedOption == 1):
        depositOperation()

    elif(selectedOption == 2):
        withdrawalOperation()

    elif(selectedOption == 3):
        customerServiceOperation()

    elif(selectedOption == 4):
        login()

    elif(selectedOption == 5):
        pass

    else:
        print("Invalid option selected")
        bankOperation(user)


def withdrawalOperation():
    print("withdrawal")
    amount = int(input('How much would you like to withdraw?\n'))
    print('Take your cash %s' %amount)


def depositOperation():
    print("Deposit Operations")
    amount = int(input('How much would you like to deposit?\n'))
    print('Your current balance is %s' % amount)

def customerServiceOperation():
    issue = input('What issue will you like to report?\n')
    print('Thank you for contacting us, we would get back to you shortly\n')
    

def generationAccountNumber():
    return random.randrange(1111111111,9999999999)

def anotherTraction():
    answer = int(input('would you like to perform another transaction? (1) Yes (2) No\n'))
    if answer == 1:
        login()
    else:
        init(3)


#### ACTUAL BANKING SYSTEM #####

ask()
