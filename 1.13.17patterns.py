row = int(input("Enter the row: "))

for x in range(1,row+1):
    for y in range(row-x):
        print("  ",end="")
    for z in range(1,x+1):
        print(f"{z} ",end="")
    print()