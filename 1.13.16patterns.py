row = int(input("Enter the number: "))

for x in range(1,row+1):
    for y in range(1,x):
        print("  ",end="")
    for z in range(row-x+1,0,-1):
        print(f"{z}",end=" ")
    print()