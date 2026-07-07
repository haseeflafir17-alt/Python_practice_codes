visitors = set()
while True:
    print("""
1. Add Visitor
2. Remove Visitor
3. Search Visitor
4. Show All Visitors
5. Remove a Random Visitor
6. Make a Backup
7. Add Multiple Visitors
8. Clear All Visitors
9. Count Visitors
10. Exit    
""")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        visit = input("Enter the visitor name to add in set: ").title()
        if visit not in visitors:
            visitors.add(visit)
            print(f"{visit} added in the set")
        else:
            print(f"{visit} already existed in the set")

    elif choice == 2:
        if len(visitors) > 0:
            visit = input("Enter the visitor name to remove from set: ").title()
            if visit in visitors:
                visitors.discard(visit)
                print(f"{visit} removed from the set")
            else:
                print(f"{visit} does not in the set")
        else:
            print("The visitor set is empty")

    elif choice ==3:
        if len(visitors) > 0:
            visit = input("Enter the visitor name to Search in set: ").title()
            if visit in visitors:
                print(f"{visit} is founded from the set")
            else:
                print(f"{visit} is not founded from the set")
        else:
            print("The visitor set is empty")

    elif choice ==4:
        if len(visitors) > 0:
            print("All visitors: ",end="")
            for v in visitors:
                print(f"{v}",end=" ")
            print()
        else:
            print("The visitor set is empty")

    elif choice ==5:
        if len(visitors) > 0:
            visitors.pop()
            print("A random visitor removed")
        else:
            print("The visitor set is empty")

    elif choice ==6:
        if len(visitors) > 0:
            visitor_copy = visitors.copy()
            print("The backup Set: ",end="")
            for vc in visitor_copy:
                print(f"{vc}",end=" ")
            print()
        else:
            print("The visitor set is empty")

    elif choice ==7:
        count = int(input("How many visitors to add: "))
        c_copy = count
        new_visit = set()
        for i in range(count):
            nv = input(f"Enter the visitor {i+1}: ").title()
            if nv in visitors:
                print(f"{nv} already existed in the set")
                c_copy -=1
            else:
                new_visit.add(nv)
        if c_copy == 0:
            print("You entered all visitors already existed so any visitors did not added now")
        elif c_copy == count:
            print(f"Successfully added {count} visitors")
            visitors.update(new_visit)
        else:
            print(f"{count-c_copy} visitors already existed, so only {c_copy} visitors added")
            visitors.update(new_visit)

    elif choice ==8:
        if len(visitors) > 0:
            sure = input("Are you sure? (yes / no) : ").lower()
            if sure == "yes":
                visitors.clear()
                print("The visitor set cleared")
            elif sure == "no":
                print("ok, The visitor set was not cleared")
            else:
                print("Invalid enter")
        else:
            print("The visitor set is empty")

    elif choice ==9:
        if len(visitors) > 0:
            print(f"Total number of visitors: {len(visitors)}")
        else:
            print("The visitor set is empty")

    elif choice ==10:
        print("Exited")
        break
    else:
        print("Invalid choice")