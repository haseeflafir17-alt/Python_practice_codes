row = int(input("Enter the number of rows u need: "))
column = int(input("Enter the number of columns u need: "))
Symbol_use = input("ENter the symbol to use: ")

for x in range (row):
    for y in range (column):
        print(Symbol_use,end=" ")
    print(end="\n")