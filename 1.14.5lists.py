Numbers = []
while True:
    print("""
1. Add numbers
2. Show all numbers
3. Show even numbers
4. Show odd numbers
5. Find largest and smallest number
6. Remove duplicate numbers
7. Sort numbers
8. Exit    
""")
    n = int(input("Enter the choice: "))
    if n == 1:
        num_count = int(input("How many numbers do you want to add? "))
        for i in range(num_count):
            num = int(input(f"Enter number {i+1} : "))
            Numbers.append(num)
        print(f"{num_count} numbers added")
    elif n == 2:
        if len(Numbers) > 0:
            print(f"All Numbers: {Numbers}")
        else:
            print("The number list Empty")
    elif n == 3:
        if len(Numbers) > 0:
            print("Even numbers: ",end="")
            even = 0
            for i in range(len(Numbers)):
                if Numbers[i] % 2 == 0:
                    print(f"{Numbers[i]}",end=" ")
                    even = 1
            if even == 0:
                print("0")
            else:
                print()
        else:
            print("The number list Empty")
    elif n == 4:
        if len(Numbers) > 0:
            print("Odd numbers: ",end="")
            odd = 0
            for i in range(len(Numbers)):
                if Numbers[i] % 2 != 0:
                    print(f"{Numbers[i]}",end=" ")
                    odd = 1
            if odd == 0:
                print("0")
            else:
                print()
        else:
            print("The number list is empty")
    elif n == 5:
        if len(Numbers) > 0:
            print(f"Largest Number: {max(Numbers)}")
            print(f"Smallest Number: {min(Numbers)}")
        else:
            print("The number list is empty")
    elif n == 6:
        if len(Numbers) > 0:
            new_list = []
            new = 0
            for number in Numbers:
                if number not in new_list:
                    new_list.append(number)
            if len(Numbers) == len(new_list):
                print("There are no duplicates")
            else:
                Numbers = new_list
                print(f"After delete duplicate: {Numbers}")
        else:
            print("The number list is empty")
    elif n == 7:
        if len(Numbers) > 0:
            Numbers.sort()
            print(f"Acending Order: {Numbers}")
            Numbers.sort(reverse=True)
            print(f"Decending Order: {Numbers}")
        else:
            print("The number list is empty")
    elif n == 8:
        print("Exit")
        break
    else:
        print("Invalid choice")
