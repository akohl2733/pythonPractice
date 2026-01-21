class MinHeap:

    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def push(self, key):
        """Insert a new key and restore heap property by bubbling up"""
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, i):
        # while not root AND parent is greater than current node
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            p = self.parent(i)
            self.swap(i, p)
            i = p
    
    def pop(self):
        if len(self.heap) == 0:
            return None
        
        root = self.heap[0]

        last_item = self.heap.pop()

        if len(self.heap) > 0:
            self.heap[0] = last_item
            self._bubble_down(0)

        return root
    
    def _bubble_down(self, i):
        min_index = 1
        left = self.left_child(i)
        right = self.right_child(i)
        n = len(self.heap)

        # check if left child exists and is smaller than current min
        if left < n and self.heap[left] < self.heap[min_index]:
            min_index = left

        # check if right child exists and is smaller than current min
        if right < n and self.heap[right] < self.heap[min_index]:
            min_index = right

        # If the smallest value is not the current node, swap and continue
        if i != min_index:
            self.swap(i, min_index)
            self._bubble_down(min_index)

    def peek(self):
        return self.heap[0] if self.heap else None
    
mh = MinHeap()
mh.push(10)
mh.push(5)
mh.push(3)  # 3 becomes root
mh.push(8)
mh.push(2)  # 2 becomes root

print(f"Root (Min): {mh.peek()}") # Should be 2
print(f"Popped: {mh.pop()}")      # Removes 2
print(f"New Root: {mh.peek()}")   # Should be 3
