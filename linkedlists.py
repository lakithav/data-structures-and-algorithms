class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class sll:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def print(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
            print()

    def insert(self,vlaue,location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                

linked_list = sll()
node1 = Node(8)
node2 = Node(15)

linked_list.head = node1
node1.next = node2
linked_list.tail = node2

linked_list.print()