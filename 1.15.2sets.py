numbers = set()
while True:
    print("""
1. Add Number
2. Remove Number
3. Search Number
4. Show All Numbers
5. Count Numbers
6. Exit
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        num = int(input("Enter the number to enter: "))
        if num not in numbers:
            numbers.add(num)
            print("Number added successfully")
        else:
            print("Number already exists.")
    elif choice == 2:
        if len(numbers) > 0:
            num = int(input("Enter the number to remove: "))
            if num in numbers:
                numbers.discard(num)
                print(f"{num} was removed")
            else:
                print("The number was already removed")
        else:
            print("Number set is empty")
    elif choice == 3:
        if len(numbers) > 0:
            num = int(input("Enter the number to Search: "))
            if num in numbers:
                print("Number found")
            else:
                print("The number did not found")
        else:
            print("Number set is empty")
    elif choice == 4:
        if len(numbers) > 0:
            print("All numbers: ",end="")
            for num in numbers:
                print(f"{num}", end=" ")
        else:
            print("Number set is empty")
    elif choice == 5:
        if len(numbers) > 0:
            print(f"Total number count: {len(numbers)}")
        else:
            print("Number set is empty")
    elif choice == 6:
        print("Exited")
        break
    else:
        print("Invalid Choice")