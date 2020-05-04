def to_base10(binary):
    binary = str(binary)
    length = len(binary)
    list_b = []
    power = length - 1
    output = 0

    for b in binary:
        int_b = int(b)
        list_b.append(int_b)

    for i in range(length):
        decimal = list_b[i] * pow(2, power)
##        print(decimal)
        power -= 1
        output = output + decimal
##        print(output)
    print("This binary converts to the decimal",output)
        

    
