class ListNode(object):

    def __init__(self, data=None, next= None):
        self._data = data
        self._next = next
        

    def __str__(self):
        """
        Note, this is a recursive method (implicit via str()). As you can see
        recursion can be used for linked data structures.
        """
        if self._data is None:
            return ''
        elif self._next is None:
            return str(self._data)
        else:
            return str(self._data) + ', ' + str(self._next)




















# print('\n\n')
# empty = ListNode()
# print('\t\tEmpty is:', empty)
# front = ListNode(1, ListNode(2, ListNode(3)))
# print('\t\tFront is:', front)
# print('\n\n')




























    # def __str__(self):
    #     output = 'ListNode(['
    #     if self._data is not None:
    #         output += str(self._data)
    #         currentnode = self._next
    #         while currentnode is not None:
    #             output += ', ' + str(currentnode._data)
    #             currentnode = currentnode._next

    #     output += '])'
    #     return output

    # def printvalues(self):
    #     if self._data is None:
    #         return
    #     else:
    #         print(str(self._data), end =' ')
    #         if self._next is not None:
    #             self._next.printvalues()

# print('\t\tValues are: ', end='')
# front.printvalues()
