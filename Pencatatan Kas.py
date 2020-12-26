balance = 600

def withdraw():  # asks for withdrawal amount, withdraws amount from balance, returns the balance amount
    counter = 0
    while counter <= 2:
        while counter == 0:
            withdraw = int(input("Enter the amount you want to withdraw: "))
            counter = counter + 1
        while ((int(balance) - int(withdraw)) < 0):
            print("Error Amount not available in card.")
            withdraw = int(input("Please enter the amount you want to withdraw again: "))
            continue
        while ((float(balance) - float(withdraw)) >= 0):
            print("Amount left in your account: " + str(balance - withdraw))
            return (balance - withdraw)
        counter = counter + 1


def deposit():
    counter = 0
    while counter <= 2:
        while counter == 0:
            deposit = int(input("Enter amount to be deposited: "))
            counter = counter + 1
        while ((int(balance) + int(deposit)) >= 0):
            print("Amount left in your account:" + str(balance + deposit))
            return (balance + deposit)
        counter = counter + 1

balance = withdraw()
balance = deposit()