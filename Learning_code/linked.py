class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = Node()

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return self.head
        else:
           temp = self.head
           while temp.next != None:
               temp.next = Node(value)
               temp = temp.next
           return temp





