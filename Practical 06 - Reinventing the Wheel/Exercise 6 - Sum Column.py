table = [[1,2,3,1],
         [4,5,6,1],
         [7,8,9,1],
         [1,2,3,4]]

def sum_column(table):
    num_tables = len(table)
    sub_list_index = 0
    column_sum_list = []
    sub_list_len = len(table[0])
    go = True

    for sub_list in table:
        if len(sub_list) != sub_list_len:
            print("None")
            go = False
            
    if go == True:
        for repeats in range(sub_list_len):
            total = 0
            for index in table:
                if sub_list_index != len(index):
                    total += index[sub_list_index]
            sub_list_index +=1
            column_sum_list.append(total)

    return(column_sum_list)

column_sum_list = sum_column(table)
print(column_sum_list)

"""
get number of sub lists
repeat for each sub list
take first index
add all first indexes together
add total to new list
repeat for next index
"""
