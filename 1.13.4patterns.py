row = int(input("Enter the row: "))

for i in range(0,row):
    for j in range(i):
        print("  ",end="")
    for j in range(row-i,0,-1):
        print("* ",end="")
    print()