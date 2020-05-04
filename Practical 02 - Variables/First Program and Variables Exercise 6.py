length_a = float(input("What is the length of triangle side A in cm?"))
length_b = float(input("What is the length of triangle side B in cm?"))
length_c = float(input("What is the length of triangle side C in cm?"))

semi_perimeter = (length_a + length_b + length_c) / 2

partial_area = (semi_perimeter * ((semi_perimeter - length_a)*(semi_perimeter - length_b)*(semi_perimeter - length_c)))
##print(partial_area)
area = round(pow(partial_area,(0.5)),3)

print("Triangle semi perimeter is", semi_perimeter, "cm")
print("Triangle Area is", area, "cm squared")
