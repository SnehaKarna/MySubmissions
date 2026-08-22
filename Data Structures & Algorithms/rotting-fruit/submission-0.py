from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()       # Stores rotten oranges
        fresh = 0             # Count fresh oranges

        # Find all rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 2:
                    queue.append((r, c))   # All rotten start together

                elif grid[r][c] == 1:
                    fresh += 1              # Count fresh orange

        minutes = 0

        # BFS continues while rotten oranges can spread
        while queue and fresh > 0:

            size = len(queue)    # Oranges rotten at start of this minute

            for _ in range(size):

                r, c = queue.popleft()     # Take one rotten orange

                directions = [
                    (1, 0),    # Down
                    (-1, 0),   # Up
                    (0, 1),    # Right
                    (0, -1)    # Left
                ]

                for dr, dc in directions:

                    nr = r + dr             # Neighbor row
                    nc = c + dc             # Neighbor column

                    # Skip if outside the grid
                    if nr < 0 or nr >= rows:
                        continue

                    if nc < 0 or nc >= cols:
                        continue

                    # Skip if neighbor is not a fresh orange
                    if grid[nr][nc] != 1:
                        continue

                    grid[nr][nc] = 2        # Make fresh orange rotten
                    fresh -= 1              # One less fresh orange

                    queue.append((nr, nc)) # Spread in next minute

            minutes += 1                   # One BFS level = 1 minute

        # Some fresh oranges could not be reached
        if fresh > 0:
            return -1

        return minutes