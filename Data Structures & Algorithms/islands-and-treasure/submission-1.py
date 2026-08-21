from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        # Put ALL treasures into the queue
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 0:
                    queue.append((r, c))

        # BFS
        while queue:

            r, c = queue.popleft()

            # Try 4 directions
            directions = [
                (1, 0),    # down
                (-1, 0),   # up
                (0, 1),   # right
                (0, -1)   # left
            ]

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Outside grid
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                # Water
                if grid[nr][nc] == -1:
                    continue

                # Already visited
                if grid[nr][nc] != 2147483647:
                    continue

                # Distance = current distance + 1
                grid[nr][nc] = grid[r][c] + 1

                # Add to queue
                queue.append((nr, nc))