#number_cakes = 6
#cake_price = 3.10
#bill = number_cakes * cake_price
#print("The price of", number_cakes, "cakes is", bill, "pounds.")

number_cakes = int(input("How many cakes did you buy?"))
cake_price = 3.10
bill = number_cakes * cake_price
if number_cakes == 1:
    print("The price of", number_cakes, "cake is", bill, "pounds.")
elif number_cakes < 1:
    print("That number of cakes is invalid!")
else:
    print("The price of", number_cakes, "cakes is", bill, "pounds.")
