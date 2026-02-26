gradebook = {}
def add_student(name, grade):
    gradebook[name] = grade
    print(name, "has been added with grade", grade)
def update_grade(name, grade):
    if name in gradebook:
        gradebook[name] = grade
        print(name, "grade has been updated to", grade)
    else:
        print("Student not found")
def display_gradebook():
    if len(gradebook) == 0:
        print("No students in the gradebook")
    else:
        print("\nStudent Gradebook:")
        for name in gradebook:
            print("Name:", name, "| Grade:", gradebook[name])
while True:
    print("\nChoose an option:")
    print("1 - Add Student")
    print("2 - Update Student Grade")
    print("3 - Show All Students")
    print("4 - Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        add_student(name, grade)
    elif choice == "2":
        name = input("Enter student name: ")
        grade = input("Enter new grade: ")
        update_grade(name, grade)
    elif choice == "3":
        display_gradebook()
    elif choice == "4":
        print("Program ended")
        break
    else:
        print("Invalid choice. Please try again.")
    
