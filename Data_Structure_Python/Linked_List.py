class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_first(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_end(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
        else:
            iteration = self.head
            while iteration.next is not None:
                iteration = iteration.next
            iteration.next = node

    def insert_at_location(self, data, position):
        node = Node(data, None)
        iteration = self.head
        count = 1
        while count <= position-2:
            iteration = iteration.next
        node.next = iteration.next
        iteration.next = node

    def remove(self, position):
        iteration = self.head
        count = 1
        if position == 1:
            self.head = iteration.next
            return
        if position - 1 == count:
            iteration.next = iteration.next.next
            return
        if position > count:
            iteration = iteration.next
            count += 1

    def print(self):
        if self.head is None:
            print('There is no data in Linked List')

        else:
            iteration = self.head
            while iteration:
                if iteration.next is not None:
                    print(f'{iteration.data}', end = '-->')

                else:
                    print(f'{iteration.data}', end = '')
                iteration = iteration.next

l = LinkedList()

l.insert_first(1)
l.insert_end(5)
l.insert_at_location(0, 2)
l.remove(1)
l.print()


