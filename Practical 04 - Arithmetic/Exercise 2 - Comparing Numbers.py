num_a = input("Enter a number: ")
num_b = input("Enter another number: ")
int_a = int(num_a)
int_b = int(num_b)
list_a = []
list_b = []
output = []
index = 0

for m in num_a:
    list_a.append(m)

for n in num_b:
    list_b.append(n)

print(list_a)
print(list_b)

if int_a > int_b:
    difference = len(list_a) - len(list_b)
    for k in range(difference):
        list_b.append(' ')
    for i in list_a:
        if list_a[index] == list_b[index]:
            output.append(1)
        else:
            output.append(0)
        index += 1
else:
    difference = len(list_b) - len(list_a)
    for k in range(difference):
        list_a.append(' ')
    for i in list_b:
        if list_b[index] == list_a[index]:
            output.append(1)
        else:
            output.append(0)
        index += 1
print(output)
