class Node:
    def __init__(self, data, next=None):
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
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def add_values(self, data_list):
        self.head = None
        for data in data_list:
             self.add_to_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid entry of index.")

        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Not a valid index")

        if index == 0:
            node = Node(data, self.head)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            count += 1
            itr = itr.next
    
    def print(self):
        if self.head == None:
            print("This Linked List is Empty.")

        result = ""
        itr = self.head
        while itr:
            result += str(itr.data) + " ---> "
            itr = itr.next

        print(str(result) + "None")


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_to_beginning(10)
    ll.print()