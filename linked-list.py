class Node:
    def __init__(self, data=None) -> None:
        """Initializes a Node object.
        >>> x=Node(1)
        >>> print(x)
        1
        """
        self.next = None
        self.data = data

    def __str__(self) -> str:
        """Prints the node data.
        >>> x=Node(3)
        >>> x.data
        3
        """
        return str(self.data)

class LinkedList:
    def __init__(self, *args) -> None:
        """Initializes a LinkedList.
        >>> l=LinkedList()
        >>> l.print()
        []
        """
        self.head = None
        self.tail = None
        for arg in args:
            self.append(arg)

    def __str__(self) -> str:
        """Print the list in the format [num1->num2].
        >>> LinkedList(1, 2, 3).print()
        [1->2->3]
        """
        if self.head == None:
            return '[]'
        to_append = ''
        curr = self.head
        while curr is not None:
            to_append += str(curr.data) + "->"
            curr = curr.next
        to_append = "[" + to_append[:-2] + "]"
        return to_append

    def __len__(self) -> int:
        """Get the length of the list.
        >>> l=LinkedList()
        >>> l.length()
        0
        >>> x=l.append(5)
        >>> len(l)
        1
        """
        curr = self.head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count
    
    def length(self) -> int:
        return self.__len__()
    
    def print(self) -> None:
        print(self.__str__())

    def append(self, x) -> None:
        """Add values to the end of the list.
        >>> LinkedList(5, 2, 7, 3).length()
        4
        """
        x = Node(x) if not isinstance(x, Node) else x
        if self.head == None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

    def prepend(self, x) -> None:
        """Add values to the beginning of the list.
        >>> l=LinkedList(5, 2)
        >>> l.prepend(100)
        >>> l.print()
        [100->5->2]
        """
        x = Node(x) if not isinstance(x, Node) else x
        x.next = self.head
        self.head = x

    def find(self, x) -> None:
        """Find the index of a element inside the list. If not found returns -1.
        >>> l=LinkedList(5, 24, 93, 6)
        >>> l.find(999)
        -1
        >>> l.find(93)
        2
        """
        curr = self.head
        idx = 0
        while curr is not None:
            if curr.data == x:
                return idx
            idx += 1
            curr = curr.next
        return -1

    def remove(self, x) -> None:
        """Remove a given element from the list
        >>> l=LinkedList(2, 3, 4)
        >>> l.remove(3)
        >>> l.print()
        [2->4]
        >>> l.remove(4)
        >>> l.print()
        [2]
        """
        prev = None
        curr = self.head

        # if head node is x
        if curr is not None:
            if curr.data == x:
                self.head = curr.next
                curr = None
                return

        # search for x
        while curr is not None:
            if curr.data == x:
                break
            prev = curr
            curr = curr.next
                
        # if x was not found
        if curr == None:
            return
        
        # unlink the node from the list
        prev.next = curr.next
        curr = None

    def reset(self) -> None:
        self._list = LinkedList()
    
    def reverse(self, curr=None, prev=None) -> None:
        """Reverse the sequence of the list
        >>> l=LinkedList(1,2,3,4)
        >>> l.reverse()
        >>> l.print()
        [4->3->2->1]
        """
        # initializing curr for the first call
        if curr is None: 
            curr = self.head

        # if the list is empty
        if self.head == None: 
            return

        # when it reaches the end of the list
        elif curr.next == None:
            self.tail == self.head
            curr.next = prev
            self.head = curr
            return

        # when it is iterating over the list
        else:
            next = curr.next
            curr.next = prev
            self.reverse(next, curr)


if __name__ == "__main__":
    import doctest
    doctest.testmod()