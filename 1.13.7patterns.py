row = int(input("Enter the number: "))

for x in range(row):
    for y in range(row-x,1,-1):
        print("  ",end="")
    for z in range(2 * x+1):
        print("* ",end="")
    print()
for x in range(row,1,-1):
    for y in range(row-x+1):
        print("  ",end="")
    for z in range(2 * x -3):
        print("* ",end="")
    print()
