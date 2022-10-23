from node import Node


class CircularLinkedList:
    # calls the parent class's constructor function

    def __init__(self) -> None:
        # contains the address of the 1st element
        self.head = None

        # contains the address of the last element
        self.tail = None

        # contains the number of elements in the list
        self.__length__ = 0

    # private method that links the tail with the head

    def __linkAsCircle__(self, outerObj: 'CircularLinkedList' = None) -> None:
        if not outerObj:
            self.tail.next = self.head
        else:
            outerObj.tail.next = outerObj.head
            return outerObj

    # This function returns the length of the list

    def __len__(self) -> int:
        return self.__length__

    # This function can be used to insert an element to the top of the linked list

    def appendFirst(self, data: any = None, next=None) -> None:
        self.__length__ += 1
        node = Node(data=data, next=self.head)
        self.head = node
        if not self.tail:
            self.tail = node
        if self.head != self.tail:
            self.__linkAsCircle__()

    # This function can be used to insert an element to the end of the linked list

    def appendLast(self, data: any = None) -> None:
        self.__length__ += 1
        node = Node(data=data)
        if not self.head:
            self.head = node

        if not self.tail:
            self.tail = node

        else:
            self.tail.next = node
            self.tail = node
        self.__linkAsCircle__()

    # This function can be used to insert an element at the specified index of the linked list

    def insert(self, data: any = None, position: int = None) -> None:
        if position == 0:
            self.appendFirst(data)
            return

        elif not position or position >= self.__length__:
            self.appendLast(data)
            return

        elif position < 0:
            raise IndexError("List index out of range")

        else:
            self.__length__ += 1
            index = 0
            iter = self.head
            while index != position - 1:
                iter = iter.next
                index += 1
            node = Node(data=data, next=iter.next)
            # node.next = iter.next
            iter.next = node
        self.__linkAsCircle__()

    # This function is used to remove an element at the specified index of the linked list

    def remove(self, position: int = None) -> None:
        if position == 0:
            self.head = self.head.next
            return

        elif not position:
            raise TypeError("Required datatype is 'int' but 'None' given")

        elif position < 0 or position > self.__length__:
            raise IndexError("List index out of range")

        else:
            index = 0
            iter = self.head
            while index != position - 1:
                iter = iter.next
                index += 1
            iter.next = iter.next.next if iter.next.next else None
            if not iter.next:
                self.tail = iter
        self.__linkAsCircle__()

    # This function will return a sliced part of the Linked list

    def slice(self, fromIndex: int = 0, toIndex: int = None) -> 'CircularLinkedList':
        if (not toIndex) or toIndex > self.__length__:
            toIndex = self.__length__
        slicedList = CircularLinkedList()
        index = 0
        shouldRun = True
        iter = self.head
        while shouldRun:
            if index >= fromIndex and index < toIndex:
                slicedList.appendLast(iter.data)
            if index >= toIndex - 1:
                shouldRun = False
            iter = iter.next
            index += 1

        return self.__linkAsCircle__(slicedList)

    # This function is used to get the element in the specified index

    def get(self, position: int = None) -> 'CircularLinkedList.data':
        if position == 0:
            return self.head.data

        elif not position:
            raise TypeError("Expected type 'int' got 'None'")

        elif position < 0 or position >= self.__length__:
            raise IndexError("List index out of range")

        elif position == self.__length__ - 1:
            return self.tail.data

        else:
            index = 0
            iter = self.head
            while index < position:
                iter = iter.next
                index += 1
            return iter.data

    # This function is used to set the element in the specified index

    def set(self, newData: any = None, position: int = None) -> None:
        if position == 0 and newData:
            self.head.data = newData

        elif not position or not newData:
            raise TypeError("Expected 'data' got 'None'")

        elif position < 0 or position >= self.__length__:
            raise IndexError("List index out of range")

        elif position == self.__length__ - 1:
            self.tail.data = newData

        else:
            index = 0
            iter = self.head
            while index < position:
                iter = iter.next
                index += 1
            iter.data = newData

    # This function will return reversed version of the Linked list

    def reverse(self) -> 'CircularLinkedList':
        # The below super fn will return a LinkedList object
        reversedList = CircularLinkedList()
        try:
            iteratorObj = iter(self)
            for data in iteratorObj:
                reversedList.appendFirst(data)
        except IndexError:
            # converting that LinkedList object to CircularLinkedList object
            return self.__linkAsCircle__(reversedList)

    # This functin will return the current length of the linked list

    def leng(self) -> int:
        return self.__length__

    # This function is used to return the string representation of the linked list
    # This is used when we print the instance of this class

    def __repr__(self) -> str:
        iter = self.head
        output = str(iter.data) + '(H)'
        iter = iter.next
        while iter.next != self.head:
            output += f" -> {iter.data}"
            iter = iter.next

        return output + ' -> H'

    # create an iterable of this object

    def __iter__(self) -> 'CircularLinkedList':
        self.current = self.head
        return self

    # get the next value in the iterable

    def __next__(self) -> 'CircularLinkedList.data':
        if self.current == None:
            raise IndexError("Index out of range")
        else:
            value = self.current.data
            self.current = None if self.current.next == self.head else self.current.next
            return value


ll = CircularLinkedList()
# print(dir(CircularLinkedList))
ll.appendFirst(10)
ll.appendFirst(20)
ll.appendFirst(30)
ll.appendFirst(40)
ll.appendLast(20)
ll.insert(15, 1)
ll.insert(21, 2)
ll.insert(211, 0)
ll.insert(217)
ll.insert(216)
ll.insert(215)
ll.insert(214)
ll.insert(213)
print(ll)
# l = ll.reverse()
# print(l)
