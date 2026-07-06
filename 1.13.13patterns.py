row = int(input("Enter the row: "))
x=1
for i in range(1,row+1):
    for j in range(1,i+1):
        print(f"{x:2}",end=" ")
        x +=1
    print()
