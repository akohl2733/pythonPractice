
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
    
    def length(self):
        curr = self.head
        total_node = 0
        while curr.next != None:
            total_node += 1
            curr = curr.next
        return total_node

    def display(self):
        elems = []
        curr = self.head
        while curr.next != None:
            curr = curr.next
            elems.append(curr.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR: Index out of range")
            return None
        curr_idx = 0
        curr = self.head
        while curr.next != None:
            curr = curr.next
            if curr_idx == index:
                return curr.data
            curr_idx += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR: index out of range")
            return None
        curr_idx = 0
        curr = self.head
        while True:
            last = curr
            curr = curr.next
            if curr_idx == index:
                last.next = curr.next
                return
            curr_idx += 1
        

my_ll = linked_list()
my_ll.append(10)
my_ll.append(12)
my_ll.append(1)
my_ll.append(5)
my_ll.append(100)
print(my_ll.erase(2))
my_ll.display()