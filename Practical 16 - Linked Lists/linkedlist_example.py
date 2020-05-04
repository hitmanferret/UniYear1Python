from listnode import ListNode

class LinkedList(object):

    def __init__(self):
        self._front = None

    def __str__(self):
        if self._front is None:
            return 'LinkedList([])'
        else:
            return 'LinkedList([' + str(self._front) +'])'

    def append(self, value):
        """
        As opposed to Python built-in list, we append at the front of the list
        to ensure fast append and pop. Note also that pop should remove and 
        return the front element. 
        Given the constructor provided in ListNode the code could be simplified to a single statement:
            self._front = ListNode(value, self._front)
        I have chosen to provide the longer implementation for pedagogical purpose so you can learn to manipulate references.
        """
        self._front = ListNode(value, self._front)
        # newnode = ListNode(value)
        # if self._front is None:
        #     self._front = newnode
        # else:
        #     newnode._next = self._front
        #     self._front = newnode

    def __len__(self):
        """ This method shows you how to traverse a linked list, from start to end. To traverse the list, we need to use a local variable <currentnone> to move along the list, we must not change/move the pointer _front.
        """
        count = 0
        currentnode = self._front
        while currentnode is not None:
            count += 1
            currentnode = currentnode._next
        
        return count



linkedlist = LinkedList()
print(linkedlist)
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)
print(linkedlist)
print(len(linkedlist))
