print("Shopping card system")
item = input("Enter the items to buy: ")
quantity = int(input(f"How many {item} want to buy: "))
price = float(input(f"what is the price of a {item} : "))
total = quantity * price
print(f"You got {quantity} x {item} ")
print(f"So, the total price is : {total}")