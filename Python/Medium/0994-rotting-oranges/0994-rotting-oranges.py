from typing import List
from collections import deque

def min_minutes_to_rot(grid: List[List[int]]) -> int:
    """
    Given a grid of oranges where:
      0 = empty cell
      1 = fresh orange
      2 = rotten orange

    Every minute, any fresh orange that is 4-directionally adjacent
    to a rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse until no
    cell has a fresh orange. If this is impossible, return -1.
    """
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    freshCount = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                freshCount += 1

    minutes = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue and freshCount > 0:
        minutes += 1

        for _ in range(len(queue)):
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    freshCount -= 1
                    queue.append((nr, nc))
                    grid[nr][nc] = 2

    if freshCount == 0:
        return minutes
    else:
        return -1
