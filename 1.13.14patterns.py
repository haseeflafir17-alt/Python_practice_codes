row = int(input("Enter the number: "))

for x in range(1,row+1):
    for y in range(1,x):
        print("  ",end="")
    for z in range(x,row+1):
        print(f"{z}",end=" ")
    print()