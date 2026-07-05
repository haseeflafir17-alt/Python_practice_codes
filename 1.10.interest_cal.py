initial_amount = 0
rate = 0
time = 0
while initial_amount<=0:
    print("Initial amount can not be less than or equal to zero!")
    initial_amount = float(input("Enter the Initial amount: "))

while rate<=0:
    print("Interest Rate can not be less than or equal to zero!")
    rate = float(input("Enter the Interest Rate: "))

while time<=0:
    print("Times in years can not be less than or equal to zero!")
    time = float(input("Enter the time in years: "))

total = initial_amount * pow((1+rate/100),time)
print(f"The final balance {time} years after is : {total:.2f}")