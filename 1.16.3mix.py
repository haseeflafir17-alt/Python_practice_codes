print("===== Student Hobby Manager =====")

students = []

while True:
    print("""
1. Add Student
2. View Students
3. Search Student
4. Add Hobby
5. Remove Hobby
6. Show Student with Most Hobbies
7. Count Total Unique Hobbies
8. Exit
""")

    choice = input("Enter your choice: ")

    # 1. Add Student
    if choice == "1":
        name = input("Enter student name: ").title()
        found = False
        for student in students:
            if student[0] == name:
                found = True
                break

        if found:
            print("Student already exists.")

        else:
            age = int(input("Enter age: "))
            hobby_count = int(input("How many hobbies? "))
            hobbies = set()
            for i in range(hobby_count):
                hobby = input(f"Enter hobby {i+1}: ").title()
                hobbies.add(hobby)

            student = (name, age, hobbies)
            students.append(student)
            print("Student added successfully.")

    # 2. View Students
    elif choice == "2":

        if students:
            print()
            for student in students:
                print("------------------------")
                print("Name :", student[0])
                print("Age  :", student[1])
                print("Hobbies:")
                for hobby in student[2]:
                    print("-", hobby)
                print("------------------------")
        else:
            print("No students available.")

    # 3. Search Student
    elif choice == "3":

        if students:
            search = input("Enter student name: ").title()
            found = False
            for student in students:
                if student[0] == search:
                    print()
                    print("Student Found")
                    print("Name :", student[0])
                    print("Age  :", student[1])
                    print("Hobbies:")
                    for hobby in student[2]:
                        print("-", hobby)
                    print("Total hobbies :", len(student[2]))
                    found = True
                    break
            if not found:
                print("Student not found.")
        else:
            print("Database is empty.")

    # 4. Add Hobby
    elif choice == "4":

        if students:
            search = input("Enter student name: ").title()
            found = False
            for student in students:
                if student[0] == search:
                    hobby = input("Enter new hobby: ").title()
                    if hobby in student[2]:
                        print("Hobby already exists.")
                    else:
                        student[2].add(hobby)
                        print("Hobby added.")
                    found = True
                    break
            if not found:
                print("Student not found.")
        else:
            print("Database is empty.")

    # 5. Remove Hobby
    elif choice == "5":
        if students:
            search = input("Enter student name: ").title()
            found = False
            for student in students:
                if student[0] == search:
                    hobby = input("Enter hobby to remove: ").title()
                    if hobby in student[2]:
                        student[2].discard(hobby)
                        print("Hobby removed.")
                    else:
                        print("Hobby not found.")
                    found = True
                    break
            if not found:
                print("Student not found.")
        else:
            print("Database is empty.")

    # 6. Student With Most Hobbies
    elif choice == "6":
        if students:
            most = students[0]
            for student in students:
                if len(student[2]) > len(most[2]):
                    most = student
            print()
            print("Student with most hobbies")
            print("Name :", most[0])
            print("Age  :", most[1])
            print("Hobbies:")
            for hobby in most[2]:
                print("-", hobby)
            print("Total hobbies :", len(most[2]))
        else:
            print("Database is empty.")

       # 7. Count Total Unique Hobbies
    elif choice == "7":
        if students:
            all_hobbies = set()
            for student in students:
                all_hobbies.update(student[2])
            print()
            print("Unique hobbies:")
            for hobby in all_hobbies:
                print("-", hobby)
            print("Total unique hobbies:", len(all_hobbies))
        else:
            print("Database is empty.")

    # 8. Exit
    elif choice == "8":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")