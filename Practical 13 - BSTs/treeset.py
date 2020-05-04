treeset = [8, [3, [1,[],[]], [6, [4,[],[]], [7,[],[]]]],
            [10,[], [14, [13,[],[]],[]]]]

def isempty(treeset):
    if treeset == []:
        return True
    else:
        return False

def isleaf(treeset):
    return not isempty(treeset) and treeset[1] == [] and treeset[2] == []

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

def get_values(treeset): #currently not working, dont really know why, probably because i suck at coding :)
    reversed_inorder_list = []
    def reverse_inorder(treeset, reversed_inorder_list):
        if isempty(treeset):
            return []
        if treeset[2] == []:
            return reversed_inorder_list.reverse()
        else:
            reverse_inorder(treeset[1], reversed_inorder_list)
            reversed_inorder_list.append(treeset[0])
            reverse_inorder(treeset[2], reversed_inorder_list)
    return reverse_inorder(treeset, reversed_inorder_list)
get_values(treeset)

def contains(element, treeset):
    pass

def equals(treeset_a, treeset_b):
    pass

def remove(element, treeset):
    pass

# def preorder(treeset):
#     if isempty(treeset):
#         return
#     else:
#         print(treeset[0])
#         preorder(treeset[1])
#         preorder(treeset[2])
# preorder(treeset)