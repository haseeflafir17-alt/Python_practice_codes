students = []

while True:
    print("""
1. Add student
2. Insert student at position
3. Remove student by name
4. Remove student by Index
5. Search student
6. Show all students
7. Replace student name
8. Exit
    """)
    choice = int(input("Enter Your choice: "))
    if choice == 1:
        student = input("Enter the name: ")
        students.append(student.capitalize())
        print(f"Student {student.capitalize()} added the list!")
    elif choice == 2:
        student = input("Enter the name: ")
        position = int(input("Enter the Index: "))
        if 0 <= position <= len(students) :
            students.insert(position,student.capitalize())
            print(f"Student {student.capitalize()} added at index {position}")
        else:
            print("Invalid Index")
    elif choice == 3:
        student = input("Enter the name to remove: ").capitalize()
        if student in students:
            students.remove(student)
            print(f"Student {student} removed from list!")
        else:
            print(f"Student {student} not found in the list")
    elif choice == 4:
        position = int (input("Enter the index to remove the student: "))
        if 0 <= position < len(students):
            std =  students.pop(position)
            print(f"Student {std} removed from index {position}")
        else:
            print("Invalid index")
    elif choice == 5:
        student = input("Enter the student name to search: ").capitalize()
        if student in students:
            print(f"Student {student} founded")
        else:
            print(f"Student {student} not found")
    elif choice == 6:
        if len(students) > 0:
            print(students)
        else:
            print("Student list is empty")
    elif choice == 7:
        old = input("Enter the old name to replace: ").capitalize()
        if old in students:
            new = input("Enter the new name to replace: ").capitalize()
            position = students.index(old)
            students.pop(position)
            students.insert(position,new)
            print(f"Old name {old} was replaced by new name {new}")
        else:
            print(f"The Old name {old} not found in the list")
    elif choice == 8:
        print("You Exited, Thank You")
        break
    else:
        print(f"You choice {choice},that is invalid ,please choice a valid one.")
