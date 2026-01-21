from collections import deque

class Graph:

    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, node1, node2, directed=False):
        self.add_node(node1)
        self.add_node(node2)

        self.adj_list[node1].append(node2)
        if not directed:
            self.adj_list[node2].append(node1)

    def DFSIterative(self, start_node):
        visited = set()
        stack = [start_node]

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                for neighbor in reversed(self.adj_list[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)

    def BFSIterative(self, start_node):
        visited = set()
        queue = deque([start_node])

        visited.add(start_node)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def display(self):
        for node, neighbors in self.adj_list.items():
            print(f"{node} -> {", ".join(map(str, neighbors))}")

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is Depth First Traversal (starting from vertex 2)")
    
    # Function call
    g.DFSIterative(2)


    print("Following is Breadth First Traversal (starting from vertex 2)")
    g.BFSIterative(2)