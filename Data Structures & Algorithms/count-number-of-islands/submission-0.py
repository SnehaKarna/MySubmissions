class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        count = 0

        def dfs(r, c):

            # Outside the grid
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Water → nothing to explore
            if grid[r][c] == "0":
                return

            # Mark this land as visited
            grid[r][c] = "0"

            # Explore all 4 directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        for r in range(rows):
            for c in range(cols):

                # Found a new island
                if grid[r][c] == "1":

                    count += 1

                    # Explore the entire island
                    dfs(r, c)

        return count