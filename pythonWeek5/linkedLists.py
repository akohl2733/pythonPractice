class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def add_to_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.add_to_end(data)

    def print(self):
        if self.head == None:
            print("Linked List is empty.")
            return
        
        itr = self.head
        res = ""
        while itr:
            res += str(itr.data) + "-->"
            itr = itr.next
        
        print(res)

    def get_length(self):

        count = 0

        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, idx):
        if idx < 0 or idx > self.get_length():
            raise Exception("Invalid index")
        
        if idx == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid value.")

        if index == 0:
            self.add_to_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1



if __name__ == "__main__":
    ll = LinkedList()
    # ll.add_to_beginning(30)
    ll.insert_values(["apple", 'orange', 'banana', 'coconut'])
    ll.remove_at(2)
    ll.insert_at(1, "grapefruit")
    print(ll.get_length())
    ll.print()