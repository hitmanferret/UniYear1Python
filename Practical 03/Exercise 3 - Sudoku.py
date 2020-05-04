n = 0
numbers_list_first = []
numbers_list_second = []
numbers_list_third = []
numbers_list_fourth = []


numbers_first = input("Enter 4 single digit numbers, each seperated by a space")
numbers_first = numbers_first.replace(" ", "|") and numbers_first.replace("0", " ")
##numbers_list_first.append(numbers_first)

numbers_second = input("Enter 4 single digit numbers, each seperated by a space")
numbers_second = numbers_second.replace(" ", "|") and numbers_second.replace("0", " ")
##numbers_list_second.append(numbers_second)

numbers_third = input("Enter 4 single digit numbers, each seperated by a space")
numbers_third = numbers_third.replace(" ", "|") and numbers_third.replace("0", " ")
##numbers_list_third.append(numbers_third)

numbers_fourth = input("Enter 4 single digit numbers, each seperated by a space")
numbers_fourth = numbers_fourth.replace(" ", "|") and numbers_fourth.replace("0", " ")
##numbers_list_fourth.append(numbers_fourth)

print("+-+-+-+-+")
print("|" + numbers_first + "|")
print("+-+-+-+-+")
print("|" + numbers_second + "|")
print("+-+-+-+-+")
print("|" + numbers_third + "|")
print("+-+-+-+-+")
print("|" + numbers_fourth + "|")
print("+-+-+-+-+")
