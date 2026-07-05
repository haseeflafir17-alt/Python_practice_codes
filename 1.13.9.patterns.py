row = int(input("Enter the rows: "))
column = int(input("Enter the columns: "))

for x in range(row):
    for y in range(column):
        if x == 0 or x== row-1 or y == 0 or y == column -1:
            print("* ", end="")
        else:
            print("  ",end="")
    print()

