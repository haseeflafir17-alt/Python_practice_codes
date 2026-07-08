foods = []
prices = []
total = 0
while True:
    food = input("Enter the food (q to quit) : ").lower()
    if food == "q":
        break
    else:
        price = float(input(f"Enter the price of {food} : "))
        foods.append(food)
        prices.append(price)

print("----------Your Cart---------")
for i in range(len(prices)):
    print(f"{foods[i]:15} : {prices[i]:.2f}")
    total += prices[i]
print()
print(f"Your Total bill : {total:.2f}")