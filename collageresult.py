students = {}

def add_marks():
    name = input("Student name: ")
    m1 = int(input("Marks 1: "))
    m2 = int(input("Marks 2: "))
    m3 = int(input("Marks 3: "))

    avg = (m1 + m2 + m3) / 3
    students[name] = avg

def show_results():
    for s in students:
        print(s, "GPA:", students[s])

while True:
    print("\n1.Add Marks 2.Show Results 3.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        add_marks()
    elif ch == 2:
        show_results()
    elif ch == 3:
        break