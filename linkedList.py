class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    def insert_at_last(self, value):
        new_node = Node(value)

        if self.start is None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def insert_at_start(self, value):
        new_node = Node(value)
        if self.start is None:
            self.start = new_node
        else:
            temp = self.start
            self.start = new_node
            new_node.next = temp

    def insert_at_specific_place(self, where, value):
        new_node = Node(value)
        counter = 1
        temp = self.start
        if where == 1:
            self.start = new_node
            new_node.next = temp
        else:
            while counter != where - 1:
                temp = temp.next
                counter += 1
            if temp.next is None:
                temp.next = new_node
                new_node.next = None
            else:
                temp2 = temp.next
                temp.next = new_node
                new_node.next = temp2

    def count_of_node(self):
        temp = self.start
        counter = 1
        while temp.next is not None:
            counter += 1
            temp = temp.next
        print(f"Length of linked list is {counter}")



    def print_linked_list(self):
        if self.start is None:
            print('Linked list is empty')
        else:
            temp = self.start
            while temp is not None:
                print(temp.data, end=' -> ')
                temp = temp.next


ll = LinkedList()
ll.insert_at_last(5)
ll.insert_at_last(100)
ll.insert_at_last(10)
ll.insert_at_start(6)
ll.insert_at_start(15)
ll.insert_at_last(69)
ll.insert_at_specific_place(6, 1000)
ll.print_linked_list()
print(end='\n')
ll.count_of_node()
