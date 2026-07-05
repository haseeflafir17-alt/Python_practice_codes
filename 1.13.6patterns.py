row = int(input("Enter the row: "))

for i in range(row,0,-1):
    for j in range(row - i, 0, -1):
        print("  ", end="")
    for k in range(2 * i - 1):
        print("* ", end="")
    print()

