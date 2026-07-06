n = int(input("Enter the number: "))

for i in range(1,n+1):
    for j in range(1,2 * n +1):
        if j == 1 or j == 2 * n or j == i or j == 2*n+1-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()

for i in reversed(range(1,n+1)):
    for j in reversed(range(1,2 * n +1)):
        if j == 1 or j == 2 * n or j == i or j == 2*n+1-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()