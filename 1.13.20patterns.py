n = int(input("Enter the number: "))

for i in range(1,n+1):
    for j in range(0,n-i):
        print("",end=" ")
    for k in range(2 * i -1):
        if k==0 or k == 2 *i -2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(n,1,-1):
    for j in range(0,n-i+1):
        print(" ",end="")
    for k in range(2 * i -3):
        if k == 0 or k == 2 * i - 4:
            print("*",end="")
        else:
            print(" ",end="")
    print()
