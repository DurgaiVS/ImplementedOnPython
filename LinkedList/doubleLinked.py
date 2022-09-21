from node import Node
from queue import Queue


class DoubleLinkedList:
    def __init__(self) -> None:
        # contains the address of the 1st element
        self.head = None

        # contains the address of the last element
        self.tail = None

        # contains the number of elements in the list
        self.length = 0

    # This function can be used to insert an element to the top of the linked list

    def appendFirst(self, data: any = None, next=None) -> None:
        self.length += 1
        node = Node(data=data, next=self.head)
        if self.head:
            self.head.previous = node
        self.head = node
        if not self.tail:
            self.tail = node

    # This function can be used to insert an element to the end of the linked list

    def appendLast(self, data: any = None) -> None:
        self.length += 1
        node = Node(data=data, previous=self.tail)
        if not self.head:
            self.head = node

        if not self.tail:
            self.tail = node

        else:
            self.tail.next = node
            self.tail = node

    # This function can be used to insert an element at the specified index of the linked list

    def insert(self, data: any = None, position: int = None) -> None:
        if position == 0:
            self.appendFirst(data)
            return

        elif not position or position >= self.length:
            self.appendLast(data)
            return

        elif position < 0:
            raise IndexError("List index out of range")

        elif position < (self.length/2):
            index = 0
            iter = self.head
            while index < position - 1:
                iter = iter.next
                index += 1
            node = Node(data=data, next=iter.next, previous=iter)
            node.next.previous = node
            iter.next = node

        else:
            index = self.length - 1
            iter = self.tail
            while index > position:
                iter = iter.previous
                index -= 1
            node = Node(data=data, next=iter, previous=iter.previous)
            iter.previous.next = node
            iter.previous = node

        self.length += 1

    # This function is used to remove an element at the specified index of the linked list

    def remove(self, position: int = None) -> None:
        if position == 0:
            self.head = self.head.next
            self.head.previous = None
            return

        elif position == self.length - 1:
            self.tail = self.tail.previous
            self.next = None

        elif not position:
            raise TypeError("Required datatype is 'int' but 'None' given")

        elif position < 0 or position > self.length:
            raise IndexError("List index out of range")

        elif position < (self.length/2):
            index = 0
            iter = self.head
            while index < position - 1:
                iter = iter.next
                index += 1
            iter.next = iter.next.next if iter.next.next else None
            iter.next.previous = iter
            if not iter.next:
                self.tail = iter

        else:
            index = self.length - 1
            iter = self.tail
            while index > position:
                iter = iter.previous
                index -= 1
            iter.previous = iter.previous.previous
            iter.previous.next = iter

        self.length -= 1

    # This function will return a sliced part of the linked list

    def slice(self, fromIndex=0, toIndex=None) -> 'DoubleLinkedList':
        if (not toIndex) or toIndex > self.length:
            toIndex = self.length
        slicedList = DoubleLinkedList()
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

        return slicedList

    # This function is used to get the element in the specified index

    def get(self, position: int = None) -> None:
        if position == 0:
            return self.head.data

        elif not position:
            raise TypeError("Expected type 'int' got 'None'")

        elif position < 0 or position >= self.length:
            raise IndexError("List index out of range")

        elif position == self.length - 1:
            return self.tail.data

        elif position < (self.length/2):
            index = 0
            iter = self.head
            while index < position:
                iter = iter.next
                index += 1
            return iter.data

        else:
            index = self.length - 1
            iter = self.tail
            while index > position:
                iter = iter.previous
                index -= 1
            return iter.data

    # This function is used to set/update the element in the specified index

    def set(self, newData: any = None, position: int = None) -> None:
        if position == 0 and newData:
            self.head.data = newData

        elif not position or not newData:
            raise TypeError("Expected 'data' got 'None'")

        elif position < 0 or position >= self.length:
            raise IndexError("List index out of range")

        elif position == self.length - 1:
            self.tail.data = newData

        elif position < (self.length/2):
            index = 0
            iter = self.head
            while index < position:
                iter = iter.next
                index += 1
            iter.data = newData

        else:
            index = self.length - 1
            iter = self.tail
            while index > position:
                iter = iter.previous
                index -= 1
            iter.data = newData

    # This function will return reversed version of the linked list

    def reverse(self) -> 'DoubleLinkedList':
        reversedList = DoubleLinkedList()
        iter = self.tail
        while iter:
            reversedList.appendLast(iter.data)
            iter = iter.previous
        return reversedList
        # output = str(iter.data)
        # iter = iter.previous
        # while iter:
        #   output += f" - {iter.data}"
        #   iter = iter.previous

        # return output

    # This function is used to return the string representation of the linked list
    # This is used when we print the instance of this class

    def __repr__(self) -> str:
        iter = self.head
        output = str(iter.data)
        iter = iter.next
        while iter:
            output += f" - {iter.data}"
            iter = iter.next

        return output

    # create an iterable of this object

    def __iter__(self) -> "DoubleLinkedList":
        self.current = self.head
        return self

    # get the next value in the iterable

    def __next__(self) -> "DoubleLinkedList.data":
        if self.current == None:
            raise IndexError("Index out of bound")
        else:
            value = self.current.data
            self.current = self.current.next
            return value


ll = DoubleLinkedList()
ll.appendFirst(10)
ll.appendLast(20)
ll.insert(15, 1)
ll.insert(115, 1)
ll.insert(125)
ll.insert(135, 3)
ll.insert(145)
ll.insert(21, 2)
ll.insert(211, 0)
ll.insert(212)
ll.insert(213)
print(ll, ll.length)
l = ll.slice()
print(l)
# print(ll.get(2))
# ll.set(220, 2)
# print(ll, ll.length)
# ll.remove(3)
print(ll.reverse())
# ll.insert(214)
# ll.insert(215)
# ll.insert(216)
# ll.insert(217)
# ll.insert(218)
# ll.insert(219, 10)
# print(ll.get(2), '1')
# ll.set(2, 2)
# print(ll)
