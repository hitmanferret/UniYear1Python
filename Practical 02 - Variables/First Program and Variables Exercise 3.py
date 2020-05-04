#Exercise 3

conversion_desired = int(input("Which weight conversion do you wish to use? Answer with 1 for Stone and Pounds to Kilograms. Answer with 2 for Kilograms to Stone and Pounds."))
if conversion_desired == 1: #runs conversion of stone + pounds to kilograms
    stones = int(input("How many stone do you weigh? (rounded down to a whole number)"))
    pounds = int(input("How many pounds are remaining?"))
    kilograms = (stones * 6.35) + (pounds / 2.21)
    print("Your converted weight is", kilograms, "kilograms")
elif conversion_desired == 2: #runs conversion of kilograms to stone + pounds
    kilograms = float(input("What is your weight in kilograms?"))
    stones = (kilograms // 6.35)
    stones_remainder = (kilograms % 6.35)
    pounds = (stones_remainder * 2.21)
    print("Your converted weight is", stones, "stone and", pounds, "pounds")
else: #catches exceptions
    print("You have entered an invalid number.")
