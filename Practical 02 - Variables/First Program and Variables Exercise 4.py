banana_kilograms = float(input("How many kilograms of bananas do you wish to order?"))
cost_kilograms = (banana_kilograms * 3)
#cost of P&P
if cost_kilograms < 50.00:
    post_cost = 4.99
else:
    post_cost = 3.49
#cost of order
banana_cost = round((banana_kilograms * 3.00), 2)
total_cost = round((banana_cost + post_cost), 2)

print("Cost before post and packaging is", banana_cost, "pounds.")
print("Cost after post and packaging is", total_cost, "pounds.")
