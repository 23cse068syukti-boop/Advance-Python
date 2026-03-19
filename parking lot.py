parking = {}

while True:
    print("\n---- Parking Lot Menu ----")
    print("1. Vehicle Entry")
    print("2. Vehicle Exit")
    print("3. Show Parked Vehicles")
    print("4. Exit Program")

    choice = input("Enter your choice (1-4): ")

    # Vehicle Entry
    if choice == "1":
        number = input("Enter vehicle number: ")
        time = int(input("Enter entry time (hour): "))
        parking[number] = time
        print("Vehicle parked successfully.")

    # Vehicle Exit
    elif choice == "2":
        number = input("Enter vehicle number: ")
        if number in parking:
            exit_time = int(input("Enter exit time (hour): "))
            fee = (exit_time - parking[number]) * 20
            print("Parking fee:", fee)
            del parking[number]
        else:
            print("Vehicle not found.")

    # Show parked vehicles
    elif choice == "3":
        if parking:
            print("Parked Vehicles:")
            for v in parking:
                print(v, "entered at", parking[v])
        else:
            print("No vehicles parked.")

    # Exit
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please select 1-4.")