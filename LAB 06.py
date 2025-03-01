from collections import deque

def vacuum_cleaner(grid, start):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    queue = deque([start])
    path = []

    while queue:
        x, y = queue.popleft()
        if grid[x][y] == 1:
            grid[x][y] = 0  
            path.append((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                queue.append((nx, ny))

    return path
room = [[1, 0], [1, 1]]
start_position = (0, 0)

cleaning_path = vacuum_cleaner(room, start_position)
print("Cleaning Path:", cleaning_path)
