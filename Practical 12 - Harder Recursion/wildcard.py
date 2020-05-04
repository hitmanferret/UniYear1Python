"""
input wildcard (0?11?00?1?)
replace ?s with 0 or 1 (not randomly)
if combination already exists, replace with opposite number, if that exists move onto another digit
output all possible combinations
"""

"""
check if 0 or 1, keep it where it is
check if ?, change to 0 or 1
check if at the end and save combination if at end
repeat, each time checking if it is a combination already created
if every digit has been checked with both 0 and 1, then return all new wildcards
"""

"""
check how many ?s
create combination
add combination to list
create new combination
add to list if not already present
once combinations is equal to 2**(num of ?s) return these combinations back into wildcard format
add to new_wildcard_list
return list
"""

def wildcard_pattern(wildcard):
    if wildcard == "":
        return ("Wildcard is empty")
    index = 0
    new_wildcard = ""
    new_wildcard_list = []
    wildcard_list_index = 0
    wildcard_index_tracker = []
    random_count = 0
    def wildcard_filler(wildcard, index, new_wildcard, wildcard_index_tracker, new_wildcard_list, wildcard_list_index, random_count):
        if index == len(wildcard):
            new_wildcard_list.append(new_wildcard)
            wildcard_list_index += 1
            index = 0
            new_wildcard = ""
            if len(new_wildcard_list) == (2**random_count):
                return new_wildcard_list

        if wildcard[index] == "0" or wildcard[index] == "1":
            new_wildcard += wildcard[index]
            wildcard_index_tracker.append(wildcard[index])
            index += 1
            return wildcard_filler(wildcard, index, new_wildcard, wildcard_index_tracker, new_wildcard_list, wildcard_list_index, random_count)
        elif wildcard[index] == "?":
            if wildcard_list_index == 0:
                random_count += 1
            wildcard_index_tracker.append("")

        if wildcard_index_tracker[index] == "":
            wildcard_index_tracker[index] = 0
            new_wildcard += "0"
        elif wildcard_index_tracker[index] == 0:
            wildcard_index_tracker[index] = 1
            new_wildcard += "1"
        elif wildcard_index_tracker[index] == 1:
            index += 1
            return wildcard_filler(wildcard, index, new_wildcard, wildcard_index_tracker, new_wildcard_list, wildcard_list_index, random_count)
    return wildcard_filler(wildcard, index, new_wildcard, wildcard_index_tracker, new_wildcard_list, wildcard_list_index, random_count)
