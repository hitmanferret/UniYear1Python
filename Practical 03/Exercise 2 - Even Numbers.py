numbers = input("Enter a series of numbers, each seperated by a space:")
integers_list = []
even_list = []
odd_list = []
even = 0
odd = 0
distinct = 0
integers = numbers.replace(" ", "")
integers = list(integers)
##print(integers)


integers_list.append(integers)


for x in integers:
    x = int(x)
    if x % 2 == 0:
        even += 1
        if x in even_list:
            pass
        else:
            even_list.append(x)
            distinct += 1
    else:
        odd_list.append(x)
        odd += 1

print("There are", distinct, " distinct even numbers, they are:", even_list)
##print("There are", o, "odd numbers, they are:", odd_list)
