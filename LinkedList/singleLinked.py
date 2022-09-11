from node import Node

class SingleLinkedList:
  def __init__(self) -> None:
    #contains the address of the 1st element
    self.head = None

    #contains the address of the last element
    self.tail = None

    #contains the number of elements in the list
    self.length = 0


  #This function can be used to insert an element to the top of the linked list
  def appendFirst(self, data : any = None, next = None) -> None:
    self.length += 1
    node = Node(data=data, next=self.head)
    self.head = node 
    if not self.tail: self.tail = node


  #This function can be used to insert an element to the end of the linked list
  def appendLast(self, data : any = None) -> None:
    self.length += 1
    node = Node(data=data)
    if not self.head: self.head = node

    if not self.tail: self.tail = node

    else:
      self.tail.next = node
      self.tail = node


  #This function can be used to insert an element at the specified index of the linked list
  def insert(self, data : any = None, position : int = None) -> None:
    if position == 0:
      self.appendFirst(data)
      return

    elif not position or position >= self.length:
      self.appendLast(data)
      return

    elif position < 0:
      raise IndexError("List index out of range")

    else:
      self.length += 1
      index = 0
      iter = self.head
      while index != position - 1:
        iter = iter.next
        index += 1
      node = Node(data=data, next=iter.next)
      # node.next = iter.next
      iter.next = node


  #This function is used to remove an element at the specified index of the linked list
  def remove(self, position : int = None) -> None:
    if position == 0:
      self.head = self.head.next
      return

    elif not position:
      raise TypeError("Required datatype is 'int' but 'None' given")

    elif position < 0 or position > self.length:
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


  #This function will return a sliced part of the Linked list
  def slice(self, fromIndex = 0, toIndex = None) -> 'SingleLinkedList':
    if (not toIndex) or toIndex > self.length: toIndex = self.length
    slicedList = SingleLinkedList()
    index = 0
    shouldRun = True
    iter = self.head
    while shouldRun:
      if index >= fromIndex and index < toIndex:
        slicedList.appendLast(iter.data)
      if index >= toIndex - 1: shouldRun = False
      iter = iter.next
      index += 1

    return slicedList


  #This function is used to get the element in the specified index
  def get(self, position : int = None) -> None:
    if position == 0: return self.head.data

    elif not position: raise TypeError("Expected type 'int' got 'None'")

    elif position < 0 or position >= self.length: raise IndexError("List index out of range")

    elif position == self.length - 1: return self.tail.data

    else:
      index = 0
      iter = self.head
      while index < position:
        iter = iter.next
        index += 1
      return iter.data


  #This function is used to set the element in the specified index
  def set(self, newData: any = None, position : int = None) -> None:
    if position == 0 and newData: self.head.data = newData

    elif not position or not newData: raise TypeError("Expected 'data' got 'None'")

    elif position < 0 or position >= self.length: raise IndexError("List index out of range")

    elif position == self.length - 1: self.tail.data = newData

    else:
      index = 0
      iter = self.head
      while index < position:
        iter = iter.next
        index += 1
      iter.data = newData


  #This function will return reversed version of the Linked list
  def reverse(self) -> 'SingleLinkedList':
    data = []
    iter = self.head
    while iter:
      data.append(iter.data)
      iter = iter.next

    reversedList = SingleLinkedList()
    while data.__len__():
      reversedList.appendLast(data.pop())

    return reversedList


  #This function is used to return the string representation of the linked list
  #This is used when we print the instance of this class
  def __repr__(self) -> str:
    iter = self.head
    output = str(iter.data)
    iter = iter.next
    while iter:
      output += f" -> {iter.data}"
      iter = iter.next

    return output



ll = SingleLinkedList()
# ll.appendFirst(10)
# ll.appendLast(20)
ll.insert(15, 1)
ll.insert(21, 2)
ll.insert(211, 0)
ll.insert(217)
ll.insert(216)
ll.insert(215)
ll.insert(214)
ll.insert(213)
ll.insert(211)
print(ll)
print(ll.slice(2, 9))
# l = ll.reverse()
# print(l.length)
# print(l)
# print(ll.get(2), '1')
# ll.set(2, 2)
# print(ll)
