unit = input("Is temperature in Celsius or Fahrenheit (C / F): ")
temp = float(input("Enter the temperature: "))
if unit == "C":
    temp2 = (temp*9/5)+ 32
    print(f"{temp} Celsius is {round(temp2,3)} Fahrenheit")
elif unit == "F":
    temp2 = (temp -32)*5/9
    print(f"{temp} Fahrenheit is {round(temp2, 3)} Celsius")
else:
    print(f"{unit} is not valid")
