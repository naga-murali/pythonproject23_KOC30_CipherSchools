'''Replica of working of ATM for a single user, we will program the next steps he may want to perform'''

import random
'''Mr. John have already logged into his account so password is not set and program after login is created'''
def substract(accountbalance, amount):
    return accountbalance - amount

def add(accountbalance, amount):
    return accountbalance + amount

def withdraw(accountbalance, amount):
    newbalance = substract(accountbalance, amount)
    return newbalance

def deposit(accountbalance, amount):
    newbalance = add(accountbalance, amount)
    return newbalance

def end():
    print("_______________________________________________\n\nTHANK YOU FOR BANKING WITH US.")
    print("_______________________________________________ \n")

def atm():
    print("_______________________________________________\n")
    name = print("WELCOME TO ATM")
    print("_______________________________________________\n")

    balance = random.randint(1000,10000)
    print("Mr. JOHN | ACCOUNTBALANCE:",balance)
    while True:
        money = input("_______________________________________________\n\n1: WITHDRAW \n2: DEPOSIT\n3: EXIT \n_______________________________________________\n\nENTER YOUR CHOICE: ")
        if money == "1":
            user_withdraw = int(input("_______________________________________________\n\nENTER THE AMOUNT YOU WANT TO WITHDRAW: ₹"))
            if user_withdraw < balance:
                print('\n'+ f"_______________________________________________\n\nYOU HAVE WITHDRAW ₹{user_withdraw} FROM YOUR ACCOUNT.")
                balance = withdraw(balance, user_withdraw)
                print(f"\n_______________________________________________\n\nYOUR BALANCE AFTER WITHDRAWL IS: ₹{balance}")
                if balance < 5000:
                    print("_______________________________________________\n\nLOW BALANCE")
                else:
                    print("_______________________________________________\n\nHIGH BALANCE")
                end()
            else:
                print("_______________________________________________\n\nYOU DON'T HAVE SUFFICIENT FUNDS.")
                end()
        elif money == "2":
            user_deposit = int(input("_______________________________________________\n\nENTER THE AMOUNT YOU WISH TO DEPOSIT: ₹"))
            print(f"_______________________________________________\n\nYOU HAVE DEPOSITED ₹{user_deposit} TO YOUR ACCOUNT.")
            balance=deposit(balance, user_deposit)
            print(f"_______________________________________________\n\nYOUR BALANCE AFTER DEPOSIT IS: ₹{balance}")
            if balance < 5000:
                print("_______________________________________________\n\nLOW BALANCE")
            else:
                print("_______________________________________________\n\nHIGH BALANCE")
            end()
        else:
            end()
        break
atm()
