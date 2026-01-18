class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, key):
        if not self.head:
            return
        
        if self.head.val[0] == key:
            self.head = self.head.next
            return

        prev = self.head
        curr = self.head.next

        while curr:
            if curr.val[0] == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def display(self):
        curr = self.head
        output = ""
        while curr:
            output += f"{curr.val} -> "
            curr = curr.next
        return output + "None"


class HashMap:

    def __init__(self):
        self.map = [None for _ in range(10)]
        self.map_size = len(self.map)
    
    def __setitem__(self, key, value):
        remainder = self._get_score(key)
        if self.map[remainder] == None:
            self.map[remainder] = LinkedList()
            self.map[remainder].append((key, value))
            return   
        if self._if_exists((key, value), self.map[remainder]) is not False:
            return
        self.map[remainder].prepend((key, value))
        return
    
    def __getitem__(self, key):
        remainder = self._get_score(key)
        if self.map[remainder] is not None:
            curr = self.map[remainder].head
            while curr:
                if curr.val[0] == key:
                    return curr.val[1]
                curr = curr.next
        print(f"Unable to locate: '{key}'")
        return None
    
    def __delitem__(self, key):
        remainder = self._get_score(key)
        if self.map[remainder] is not None:
            self.map[remainder].remove(key)
            return
        print(f"Unable to locate: '{key}'")
        return None    

    def _get_score(self, key):
        total_score = 0
        str_data = str(key)
        for char in str_data:
            total_score += ord(char)
        remainder = total_score % self.map_size
        return remainder


    def _if_exists(self, data, ll: LinkedList):
        curr = ll.head
        while curr:
            if curr.val[0] == data[0]:
                curr.val = (data[0], data[1])
                return curr.val
            curr = curr.next
        return False
    
    def __str__(self):
        results = ""
        for i, bucket in enumerate(self.map):
            if bucket:
                results += f"Bucket {i}: {bucket.display()} -> ...\n"
        return results


mapper = HashMap()
mapper["pigeon"] = 5
mapper["bear"] = 10
mapper["chicken"] = 10
mapper["bird"] = 10
mapper["duck"] = 10
mapper["cat"] = 10
mapper["ostrich"] = 10
mapper["feline"] = 10
mapper["rhino"] = 10
mapper["zebra"] = 10
mapper["eagle"] = 10
mapper["manta ray"] = 10
mapper["elephant"] = 10
del mapper["cat"]
del mapper["chicken"]
del mapper["hippo"]
print(mapper)