weight = float(input("Enter the weight: "))
unit = input("Enter the unit (Kilogram or Pounds) {K / P}")
if weight>0:
    if unit == "K":
        new_weight = weight * 2.205
        print(f"{round(weight,3)} Kg is {round(new_weight,3)} Pounds")
    elif unit == "P":
        new_weight = weight / 2.205
        print(f"{round(weight, 3)} Pounds is {round(new_weight, 3)} Kg")
    else:
        print(f"You entered a wrong unit {unit}, please enter a correct unit!")
else:
    print("Enter a valid weight")

print("Thank you!")