n = int(input("Enter the number: "))
for x in range (n,0,-1):
    for y in range(0,n-x,1):
        print("  ",end="")
    for z in range(2 * x -1):
        print("* ",end="")
    print()


for x in range(n-1):
    for y in range(n-1,x+1,-1):
        print("  ",end="")
    for z in range(2 * x + 3):
        print("* ",end="")
    print()