rows = int(input("Input a number of rows: "))
rows = rows + 1
output = ("")
number = 0

for i in range(rows):
    repeats = i
    output = ("")
    for j in range(repeats):
        number += 1
        output += (" " + str(number))
    print(output)
    
