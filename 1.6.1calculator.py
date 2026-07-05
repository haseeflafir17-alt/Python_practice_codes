operator = input("Enter the operator ( + - * / ) : ")
num1 =float(input("Enter the 1st number: "))
num2 =float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {round(result,3)}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {round(result, 3)}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {round(result, 3)}")
elif operator == "/":
    if num2>0:
        result = num1 / num2
        print(f"{num1} / {num2} = {round(result, 3)}")
    else:
        print(f"Sorry the number 2 -- {num2} , you entered that is not suitable to divider,please enter a number greater than 0!")
else:
    print(f"You entered an invalid operator {operator},please enter within these (+ - * / )!")
print("Thank You")