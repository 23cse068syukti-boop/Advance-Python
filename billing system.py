products = {
    "apple": 50,
    "milk": 40,
    "bread": 30
}

total = 0

while True:
    print("\n---- Billing Menu ----")
    print("1. Show Products")
    print("2. Buy Product")
    print("3. Show Total Bill")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("\nAvailable Products:")
        for p in products:
            print(p, ":", products[p])

    elif choice == "2":
        item = input("Enter product name: ")

        if item in products:
            qty = int(input("Enter quantity: "))
            price = products[item] * qty
            total += price
            print("Item added. Cost =", price)
        else:
            print("Product not found")

    elif choice == "3":
        print("Total bill:", total)

    elif choice == "4":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice")