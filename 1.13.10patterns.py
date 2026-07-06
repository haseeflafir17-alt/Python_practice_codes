row = int(input("Enter the row: "))

for x in range (1,row+1):
    for y in range(x):
        if y == 0 or y == x-1 or x==row:
            print("* ",end="")
        else:
            print("  ",end="")
    print()