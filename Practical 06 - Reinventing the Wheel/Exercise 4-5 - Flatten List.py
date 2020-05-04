##list_2D = [[1,2,3,4],[5,6,7],[8,9]]

##def flatten(list_2D):
##    new_list = []
##    for i in list_2D:
##        for j in i:
##            new_list.append(j)
##    print(new_list)
##
##flatten(list_2D)


list_1D = [1,2,3,4,5,6,7,8,9]

def rasterise(list_1D, width):
    new_list = []
    if len(list_1D) % width == 0:
        repeats = len(list_1D) // width
        for i in range(repeats):
            new_sub_list = []
            for j in range(width):
                new_sub_list.append(list_1D[0])
                del list_1D[0]
            new_list.append(new_sub_list)
        print(new_list)
    else:
        print("None")
        
        
            


rasterise(list_1D, 3)
