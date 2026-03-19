# Available seats
seats = ["A1","A2","A3","A4","A5"]
booked_seats = []

while True:
    print("\n---- Movie Ticket Menu ----")
    print("1. Show Available Seats")
    print("2. Book a Seat")
    print("3. Show Booked Seats")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Show available seats
    if choice == "1":
        if seats:
            print("Available seats:", seats)
        else:
            print("No seats available.")

    # Book a seat
    elif choice == "2":
        seat = input("Enter seat to book: ")
        if seat in seats:
            seats.remove(seat)
            booked_seats.append(seat)
            print("Seat booked successfully:", seat)
        else:
            print("Seat not available or already booked.")

    # Show booked seats
    elif choice == "3":
        if booked_seats:
            print("Booked seats:", booked_seats)
        else:
            print("No seats booked yet.")

    # Exit program
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please enter 1-4.")