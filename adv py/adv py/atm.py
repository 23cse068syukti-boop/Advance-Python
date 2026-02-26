accounts = {}
def create_account():
    acc_no = input("Create account number: ")
    pin = input("Create PIN: ")
    balance = int(input("Enter initial balance: "))
    accounts[acc_no] = {"pin": pin, "balance": balance}
    print("Account created successfully!\n")
def check_balance(acc_no):
    print("Your balance is:", accounts[acc_no]["balance"])
def deposit(acc_no, amount):
    accounts[acc_no]["balance"] += amount
    print("Amount deposited successfully.")
    print("Updated balance:", accounts[acc_no]["balance"])

def withdraw(acc_no, amount):
    if accounts[acc_no]["balance"] >= amount:
        accounts[acc_no]["balance"] -= amount
        print("Please collect your cash.")
        print("Remaining balance:", accounts[acc_no]["balance"])
    else:
        print("Insufficient balance.")
print("Welcome to ATM")
n = int(input("How many accounts do you want to create? "))
for i in range(n):
    create_account()
acc_no = input("\nEnter your account number: ")
pin = input("Enter your PIN: ")
if acc_no in accounts and accounts[acc_no]["pin"] == pin:
    print("Login successful!")
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            check_balance(acc_no)
        elif choice == "2":
            amount = int(input("Enter amount to deposit: "))
            deposit(acc_no, amount)
        elif choice == "3":
            amount = int(input("Enter amount to withdraw: "))
            withdraw(acc_no, amount)
        elif choice == "4":
            print("Thank you for using ATM.")
            break
        else:
            print("Invalid choice.")
else:
    print("Invalid account number or PIN.")
