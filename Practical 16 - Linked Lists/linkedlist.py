from listnode import ListNode

class LinkedStack(object):

    def __init__(self):
        self._top = None

    def __str__(self):
        if self._top is None:
            return 'LinkedStack([])'
        else:
            return 'LinkedStack([' + str(self._top) + '])'
    
    def push(self, value):
        newnode = ListNode(value, self._top)
        if self._top is None:
            self._top = newnode
        else:
            newnode._next = self._top
            self._top = newnode
    
    def pop(self):
        if self._top is None:
            raise ValueError
        else:
            poppedvalue = self._top._data
            self._top = self._top._next
            return poppedvalue

    def peek(self):
        if self._top is None:
            return 'LinkedStack is Empty'
        else:
            return self._top._data
    
    def __len__(self):
        count = 0
        currentnode = self._top
        while currentnode is not None:
            count += 1
            currentnode = currentnode._next
        return count

l1 = LinkedStack()
l1.push(4)
l1.push(7)
l1.push(10)
# print(l1)
# print(len(l1))

class LinkedQueue(object):

    def __init__(self):
        self._top = None

    def __str__(self):
        if self._top is None:
            return 'LinkedQueue([])'
        else:
            return 'LinkedQueue([' + str(self._top) + '])'
    
    def enqueue(self, value):
        newnode = ListNode(value, self._top)
        if self._top is None:
            self._top = newnode
        else:
            currentnode = self._top
            count = 0
            while currentnode is not None:
                count += 1
                currentnode = currentnode._next
            for i in range(count - 1):
                currentnode = currentnode._next
                if i == count - 1:
                    currentnode = newnode
    
    def pop(self):
        if self._top is None:
            raise ValueError
        else:
            poppedvalue = self._top._data
            self._top = self._top._next
            return poppedvalue

    def peek(self):
        if self._top is None:
            return 'LinkedStack is Empty'
        else:
            return self._top._data
    
    def __len__(self):
        count = 0
        currentnode = self._top
        while currentnode is not None:
            count += 1
            currentnode = currentnode._next
        return count

q1 = LinkedQueue()
q1.enqueue(4)
print(q1)
q1.enqueue(7)
print(q1)
q1.enqueue(10)
print(q1)
# print(q1)
# q1.pop()
# print(q1)
# print(len(q1))