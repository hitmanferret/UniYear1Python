class TreeSet(object):
    def __init__(self, root = None):
        self._root = root
        self._left = None
        self._right = None
    
    def __str__(self):
        if self.isempty():
            return '[]'
        if self._left is None:
            left = '[]'
        else:
            left = str(self._left)
        if self._right is None:
            right = '[]'
        else:
            right = str(self._right)
        return '[' + str(self._root) + ',' + left + ',' + right + ']'

    def isempty(self):
        if self._root is None:
            return True
        else:
            return False

    def add(self, element):
        if element == None:
            return
        if self._root == None or self._root == element:
            self._root = element
            return
        elif element > self._root:
            if self._right == None:
                self._right = TreeSet(element)
            else:
                self._right.add(element)
        else:
            if self._left == None:
                self._left = TreeSet(element)
            else:
                self._left.add(element)
    

test = TreeSet(5)
test.add(3)
print(test)