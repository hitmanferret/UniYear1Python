rows = int(input("Input number of rows for triangle: "))
output = ("")

for i in range(rows):
    if i % 2 == 0:
        output = '1' + output
    else:
        output = '0' + output
    print(output)
