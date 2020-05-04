##year = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

##for key,val in year.items():
##    print(key, '-->', val)


dict1 = {1:'one', 2:'two', 3:'three'}
dict2 = {4:'four', 2:'seven'}

def concat_dict(dict1, dict2):
    new_dict = {}
    for key1,val1 in dict1.items():
            new_dict[key1] = val1
    for key2,val2 in dict2.items():
        new_val = []
        if key2 in new_dict.keys():
            new_val.append(new_dict[key2])
            new_val.append(val2)
            new_dict[key2] = new_val
        else:
            new_dict[key2] = val2
            
    return new_dict

new_dict = concat_dict(dict1, dict2)
print(new_dict)
