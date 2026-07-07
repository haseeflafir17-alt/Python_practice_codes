roll_numbers = (101, 102, 103, 101, 104, 105, 102, 106, 107, 108, 109, 101)
printed = set()
while True:
    print("""
1. View All Roll Numbers
2. Search Roll Number
3. Count Occurrences
4. Show First and Last Roll Number
5. Display Roll Number by Index
6. Show Total Number of Roll Numbers
7. Check Duplicate Roll Numbers
8. Try to Add a Roll Number
9. Exit
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("All roll numbers: ",end="")
        for num in roll_numbers:
            print(f"{num} ",end="")
        print()
    elif choice == 2:
        search = int(input("Enter the roll number to search: "))
        if search in roll_numbers:
            print("Roll number found")
            print(f"First index: {roll_numbers.index(search)}")
        else:
            print("Roll number not found")

    elif choice == 3:
        search = int(input("Enter the roll number to count Occurrences: "))
        if search in roll_numbers:
            print(f"Roll number: {search}")
            print(f"Occurrences: {roll_numbers.count(search)}")
        else:
            print("Occurrences: 0")

    elif choice == 4:
        print(f"First roll number: {roll_numbers[0]}")
        print(f"Last roll number: {roll_numbers[len(roll_numbers)-1]}")

    elif choice == 5:
        index = int(input("Enter the index to get roll number: "))
        if 0 <= index < len(roll_numbers):
            print(f"Roll number: {roll_numbers[index]}")
        else:
            print(f"The index/s are o to {len(roll_numbers)-1} are  available but you entered {index} ")

    elif choice == 6:
        print(f"Total number of roll numbers: {len(roll_numbers)}")

    elif choice == 7:
        for num in roll_numbers:
            if num not in printed:
                if roll_numbers.count(num) > 1:
                    printed.add(num)
        if len(printed)>0:
            print("Duplicates: ")
            for i in printed:
                print(f"{i}")
        else:
            print("There are no duplicates")

    elif choice == 8:
        new = int(input("Enter a roll number to add in the tuple: "))
        print("Tuples are immutable.\nA new roll number cannot be added after the tuple is created.")
    elif choice == 9:
        print("Exited")
        break
    else:
        print("Invalid choice")