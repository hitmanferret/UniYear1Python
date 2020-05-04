file = 'precipitations-Europe.txt'
file = open(file,'r')
file_info = file.readlines()
##print(file_info)
info_list = []
for line in file_info:
    info_list.append(str(line).strip('\n').split()) # appends everything to a list and removes \n
del(info_list[0]) # removes first comment line of text file
file.close()
        
##print(info_list)

max_year = ""
max_prec = 0
min_year = ""
min_prec = 1000000
mean_precipitation = 0
number_list = []

for i in info_list:
    for j in i:
        year = int(j[0:4])
        number = float(j[5:])
        number_list.append(number)
##        print(year,number)
        if number > max_prec:
            max_prec = number
            max_year = year
        elif number < min_prec:
            min_prec = number
            min_year = year

total_for_mean = 0
for num in number_list:
    total_for_mean += num
    mean_precipitation = total_for_mean/(len(number_list))
    mean_precipitation = round(mean_precipitation, 2)
    
print("Maximum precipitation was", max_prec, "in the year", max_year)
print("Minimum precipitation was", min_prec, "in the year", min_year)
print("Mean precipitation is", mean_precipitation)

