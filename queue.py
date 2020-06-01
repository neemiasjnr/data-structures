class Node:
    """
    >>> n=Node(5)
    >>> print(n)
    5
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

class Queue:
    """
    >>> q=Queue()
    >>> print(q)
    None
    """
    def __init__(self, *args):
        self.head = None
        self.tail = None
        for arg in args:
            self.enqueue(arg)

    def __str__(self):
        if self.head == None:
            return 'None'
        curr = self.head
        to_append = ''
        while curr is not None:
            to_append += str(curr.data) + "->"
            curr = curr.next
        return to_append[:-2]

    def enqueue(self, x):
        """
        >>> q=Queue(1,2,3)
        >>> print(q)
        1->2->3
        """
        x = x if isinstance(x, Node) else Node(x)
        if self.head == None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

    def dequeue(self):
        """
        >>> q=Queue()
        >>> q.enqueue(3)
        >>> q.dequeue()
        >>> print(q)
        None
        >>> q.enqueue(7)
        >>> q.enqueue(9)
        >>> q.enqueue(53)
        >>> q.dequeue()
        >>> print(q)
        7->9
        >>> q.dequeue()
        >>> print(q)
        7
        >>> q.dequeue()
        >>> print(q)
        None
        """
        if self.head == None:
            return
        curr = self.head
        if curr.next is None:
            self.head = None
            return

        while curr.next is not None:
            if curr.next == None:
                break
            prev = curr
            curr = curr.next

        prev.next = None
        curr = None

if __name__ == "__main__":
    import doctest
    doctest.testmod()