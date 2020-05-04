##a_string = '1 30 4 5'
##def sum_numbers(a_string):
##    total = 0
##    a_string = a_string.split()
##    for i in a_string:
##        i = int(i)
##        total += i
##    return total

def sum_from_file(filename):
    #A function that takes a file containing random numbers
    #separated by spaces and sums them together to produce
    #a total number which is then returned by the function.
    total = 0
    file = open(filename, 'r') #opens the chosen file containing numbers
    a_string = str(file.read()).split() #forms a string list of the numbers
    for i in a_string: #loops through the string list
        i = int(i) #converts strings to integers
        total += i #calculates the total
    return total

total = sum_from_file('numbers.txt')
print(total)



        
    
