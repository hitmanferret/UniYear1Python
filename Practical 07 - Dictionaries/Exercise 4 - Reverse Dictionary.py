dict1 = {"one":1, "two":2, "three":3, "four":3}

def reverse_dict(dict1):
    new_dict = {}
    for key,val in dict1.items():
        if val in new_dict.keys():
            print("Duplicate value detected and omitted")
        else:
            new_dict[val] = key
    return new_dict

new_dict = reverse_dict(dict1)
print(new_dict)
