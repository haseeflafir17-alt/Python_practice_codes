mark = int(input("Enter your mark: "))
if mark<0:
    print("You entered a negative number as mark")
elif mark>100:
    print("You entered a number higher than 100 as mark")
elif mark>=75:
    print("You got A grade")
elif mark>=65:
    print("You got B grade")
elif mark>=50:
    print("You got C grade")
elif mark>=35:
    print("You got S grade")
else:
    print("You got F grade")

print("Thank you!")