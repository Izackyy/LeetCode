from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rows, cols = len(grid), len(grid[0])
        q = deque()
        freshCount = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    freshCount += 1
        
        minutes = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q and freshCount > 0:
            minutes += 1

            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        freshCount -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
        
        if freshCount == 0:
            return minutes
        else:
            return -1