keys = ['one','two','three','four','five']
values = [1,2,3,4,4]

def map_list(keys, values):
    dictionary = {}
    for k in keys:
        if k in dictionary.keys():
            print("Duplicate Key Detected and Omitted")
        else:
            dictionary[k] = values[keys.index(k)]
    return dictionary

dictionary = map_list(keys, values)
print(dictionary)
        
