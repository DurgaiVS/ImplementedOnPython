class Node:
  def __init__(self, data = None, next = None, previous = None) -> None:
    #This is where the data is stored
    self.data = data

    #This will hold the address of the next element in the linked list
    self.next = next
    
    #This will hold the address of the previous element in the linked list
    self.previous = previous