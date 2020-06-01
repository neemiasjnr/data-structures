class Node:
    """Initialize a Node object
    >>> n=Node(5)
    >>> print(n)
    5
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self, *args):
        self.head = None
        for arg in args:
            self.push(arg)

    def is_empty(self):
        """
        >>> s=Stack()
        >>> s.is_empty()
        True
        """
        return self.head == None

    def __str__(self):
        if self.head == None:
            return 'None'
        to_append = ''
        curr = self.head
        while curr is not None:
            to_append += str(curr.data) + "\n"
            curr = curr.previous
        return to_append[:-1]
    
    def push(self, x):
        """
        >>> s=Stack(1, 2)
        >>> print(s)
        2
        1
        """
        x = x if isinstance(x, Node) else Node(x)
        if self.head == None:
            self.head = x
        else:
            x.previous = self.head
            self.head.next = x
            self.head = x

    def pop(self):
        """
        >>> s=Stack(6, 3, 1)
        >>> s.pop()
        >>> print(s)
        3
        6
        """
        self.head = self.head.previous

    def peek(self):
        """
        >>> s=Stack(1, 2, 3)
        >>> print(s.peek())
        3
        """
        return self.head

    def flush(self):
        """
        >>> s=Stack(1,2,3,4)
        >>> print(s)
        4
        3
        2
        1
        >>> s.flush()
        >>> print(s)
        None
        """
        while self.head is not None:
            self.head = self.head.previous

if __name__ == "__main__":
    import doctest
    doctest.testmod()