from collections import deque

def shortest_path(maze):
    rows = len(maze)
    cols = len(maze[0])
    
    start = (0, 0)
    target = (rows - 1, cols - 1)
    
    if maze[0][0] == 1 or maze[rows-1][cols-1] == 1:
        return -1

    queue = deque([(0, 0, 1)])
    visited = set()
    visited.add((0, 0))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:

        r, c, steps = queue.popleft()

        if r == rows-1 and c == cols-1:
            return steps

        for dr, dc in directions:
            new_r, new_c = (r + dr, c + dc)

            if 0 <= new_r < rows and 0 <= new_c < cols:
                if maze[new_r][new_c] != 1 and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c, steps + 1))

    return -1

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]
print(shortest_path(grid)) # Should print 7