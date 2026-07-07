names = []
marks = []

while True:
    print("""
1. Add Student
2. View Students
3. Search Student
4. Update Marks
5. Remove Student
6. Highest Mark
7. Lowest Mark
8. Average Mark
9. Sort Students by Marks (Highest → Lowest)
10. Clear Database
11. Exit    
""")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter the student name: ").capitalize()
        if name not in names:
            mark = int(input("Enter the mark: "))
            if 0 <= mark <= 100 :
                names.append(name)
                marks.append(mark)
                print(f"Student {name}'s mark {mark} added")
            else:
                print("Marks should be between 0 to 100")
        else:
            print(f"Student {name} already exist")
    elif choice == 2:
        if len(names) > 0:
            print("Index\tName\tMark")
            for i in range(len(names)):
                print(f"{i}\t{names[i]}\t{marks[i]}")
        else:
            print("Database is empty")
    elif choice == 3:
        if len(names) > 0:
            s_name = input("Enter the student name to search: ").capitalize()
            if s_name in names:
                print("Student found")
                print(f"Name: {names[names.index(s_name)]}")
                print(f"Mark: {marks[names.index(s_name)]}")
                print(f"Index: {names.index(s_name)}")
            else:
                print("Student not found")
        else:
            print("Database is empty")
    elif choice == 4:
        if len(names) > 0:
            s_name = input("Enter the student name to update the mark: ").capitalize()
            if s_name in names:
                mark = int(input("Enter the new mark: "))
                if 0 <= mark <= 100:
                    marks[names.index(s_name)] = mark
                    print(f"Student {names[names.index(s_name)]}'s marks updated to {marks[names.index(s_name)]}")
                else:
                    print("Marks should be between 0 to 100")
            else:
                print("Student not found")
        else:
            print("Database is empty")
    elif choice == 5:
        if len(names) > 0:
            s_name = input("Enter the student name to remove: ").capitalize()
            if s_name in names:
                n = names.index(s_name)
                print(f"{names[n]} removed")
                names.pop(n)
                marks.pop(n)
            else:
                print("Student not found")
        else:
            print("Database is empty")
    elif choice == 6:
        if len(names) > 0:
            m_mark = max(marks)
            m_n = marks.index(m_mark)
            print(f"Highest Student: {names[m_n]}")
            print(f"Mark: {marks[m_n]}")
        else:
            print("Database is empty")
    elif choice == 7:
        if len(names) > 0:
            m_mark = min(marks)
            m_n = marks.index(m_mark)
            print(f"Lowest Student: {names[m_n]}")
            print(f"Mark: {marks[m_n]}")
        else:
            print("Database is empty")
    elif choice == 8:
        if len(names) > 0:
            m_sum = sum(marks)
            avg = m_sum/len(marks)
            print(f"Average: {avg:.2f}")
        else:
            print("Database is empty")
    elif choice == 9:
        if len(names) > 0:
            for i in range(len(marks)-1):
                for j in range(len(marks)-1):
                    if marks[j] < marks[j+1]:
                        temp_m = marks[j]
                        temp_n = names[j]

                        marks[j] = marks[j+1]
                        names[j] = names[j+1]
                        marks[j+1] = temp_m
                        names[j+1] = temp_n
            print("Students sorted successfully.")

            for i in range(len(names)):
                print(names[i], marks[i])
        else:
            print("Database is empty")
    elif choice == 10:
        if len(names) > 0:
            sure = input("Are you sure? (yes/no): ").lower()
            if sure == "yes":
                print("database cleared!")
                marks.clear()
                names.clear()
            elif sure == "no":
                print("Ok, Database was not cleared")
            else:
                print("Invalid input")
        else:
            print("Database is empty")
    elif choice == 11:
        print("Exited")
        break
    else:
        print("Invalid choice")


