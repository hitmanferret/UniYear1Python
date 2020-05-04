def _isleaf(treeset):
    return treeset != [] and treeset[1] == [] and treeset[2] == []


def isempty(treeset):
    return treeset == []

def add(element, treeset):
    if isempty(treeset):
        treeset.append(element)
        treeset.append([])
        treeset.append([])
        return
    if element == treeset[0]:
        return
    elif element < treeset[0]:
        add(element, treeset[1])
    else:
        add(element, treeset[2])

def maxvalue(treeset):
    if isempty(treeset):
        return float('-inf')
    elif treeset[2] == []:
        return treeset[0]
    else:
        return maxvalue(treeset[2])

def minvalue(treeset):
    if isempty(treeset):
        return float('inf')
    elif treeset[1] == []:
        return treeset[0]
    else:
        return minvalue(treeset[1])

def get_values(treeset):
    if isempty(treeset):
        return []
    else:
        output = get_values(treeset[2])
        output += [treeset[0]]
        output += get_values(treeset[1])
        return output

def contains(element, treeset):
    if isempty(treeset):
        return False
    elif element == treeset[0]:
        return True
    elif element < treeset[0]:
        return contains(element, treeset[1])
    else:
        return contains(element, treeset[2])

def equals(treesetA, treesetB):
    return get_values(treesetA) == get_values(treesetB)

def remove(element, treeset):
    if isempty(treeset):
        return
    elif (not isempty(treeset[1])) and element < treeset[0]:
        remove(element, treeset[1])
    elif (not isempty(treeset[2])) and element > treeset[0]:
        remove(element, treeset[2])
    elif element == treeset[0]:
        if _isleaf(treeset):
            treeset.clear()
        elif isempty(treeset[1]):
            treeset[0] = treeset[2][0]
            treeset[1] = treeset[2][1]
            treeset[2] = treeset[2][2]
        elif isempty(treeset[2]):
            treeset[0] = treeset[1][0]
            treeset[2] = treeset[1][2]
            treeset[1] = treeset[1][1]
        else:
            smallest = minvalue(treeset[2])
            treeset[0] = smallest
            remove(smallest, treeset[2])
    else: # arrived at the end of a branch and did not find the element
        return

    