numbers =[]

while True:
    print("""
1. Add number
2. Insert number at position
3. Remove number by value
4. Remove number by index
5. Show list
6. Exit 
    """)
    choice = input("Enter Your Choice: ")
    if choice == "1":
        num = int(input("Enter the number: "))
        numbers.append(num)
        print(f"Number {num} was added")
    elif choice == "2":
        num = int(input("Enter the number: "))
        position = int(input(f"Enter the position to add {num}:"))
        if 0 <= position <= len(numbers):
            numbers.insert(position,num)
            print(f"Number {num} has added at index {position}")
        else:
            print("Invalid position")
    elif choice == "3":
        num = int(input("Enter the number to remove: "))
        if num in numbers:
            numbers.remove(num)
            print(f"Number {num} was removed")
        else:
            print(f"Number {num} is not found in the list to remove")
    elif choice == "4":
        position = int(input("Enter the index to delete the number: "))
        if 0 <= position < len(numbers):
            numbers.pop(position)
            print(f"Index {position}'s number removed")
        else:
            print("Invalid Index")
    elif choice == "5":
        print(numbers)
    elif choice == "6":
        print("Thank You!")
        print("You Exited")
        break
    else:
        print(f"You Entered {choice}. Which is invalid, please enter(1/6)!")