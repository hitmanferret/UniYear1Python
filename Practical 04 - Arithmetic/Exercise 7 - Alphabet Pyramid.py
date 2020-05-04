rows = int(input("Input the number of rows for the pyramid: "))
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q" ,"R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
reverse_letters = []
output = ("")
spaces = rows - 1
row = 1

for i in range(rows):
    output = ""
    this_row = []
    for j in range(row):
        this_row.append(letters[j])
    reverse_letters = this_row.copy()
    reverse_letters.reverse()
    del reverse_letters[0]
    row += 1
    for k in reverse_letters:
        this_row.append(k)
    for l in this_row:
        output += (l + " ")
    for p in range(spaces):
        output = "  " + output + "  "
    spaces -= 1
    print(output)
