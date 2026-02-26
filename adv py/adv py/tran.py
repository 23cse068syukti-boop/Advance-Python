balance = 0
transactions = []
PASSWORD = "sikha15"
def login():
    attempts = 3
    while attempts > 0:
        password = input("Enter password: ")
        if password == PASSWORD:
            print("Login successful!\n")
            return True
        else:
            attempts -= 1
            print("Wrong password! Attempts left:", attempts)
    print("Account locked.")
    return False
def deposit():
    global balance
    amount = float(input("Enter deposit amount: "))
    if amount > 0:
        balance = balance + amount
        transactions.append("Deposited: " + str(amount))
        print("Money deposited successfully!")
    else:
        print("Invalid amount!")
def withdraw():
    global balance
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance = balance - amount
        transactions.append("Withdrawn: " + str(amount))
        print("Money withdrawn successfully!")
def check_balance():
    print("Your current balance is:", balance)
def view_transactions():
    if len(transactions) == 0:
        print("No transactions yet.")
    else:
        print("\nTransaction History:")
        for item in transactions:
            print(item)
if login():
    while True:
        print("\n===== ATM MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transactions")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            check_balance()
        elif choice == "4":
            view_transactions()
        elif choice == "5":
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice! Please try again.")



