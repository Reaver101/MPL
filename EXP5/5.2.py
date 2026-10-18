class InsufficientBalance(Exception):
    pass

class InvalidAccount(Exception):
    pass

account_no = 12345
balance = 10000

acc = int(input("Enter account number: "))
amount = int(input("Enter amount to withdraw: "))

try:
    if acc != account_no:
        raise InvalidAccount

    if amount > balance:
        raise InsufficientBalance

    balance = balance - amount

    print("Withdrawal Successful")
    print("Remaining Balance =", balance)

except InvalidAccount:
    print("Invalid Account Number")

except InsufficientBalance:
    print("Insufficient Balance")