row = int(input("Enter the rows: "))

for x in range(row):
    for y in range(row):
        if x == 0 or x== row-1 or y == 0 or y == row -1:
            print("* ", end="")
        else:
            print("  ",end="")
    print()

