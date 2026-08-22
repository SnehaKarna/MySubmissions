class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):

            visited.add((r, c))

            directions = [
                (1, 0),    # down
                (-1, 0),   # up
                (0, 1),    # right
                (0, -1)   # left
            ]

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Outside grid
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                # Already visited
                if (nr, nc) in visited:
                    continue

                # Reverse flow:
                # neighbor must be >= current height
                if heights[nr][nc] < heights[r][c]:
                    continue

                dfs(nr, nc, visited)

        # Pacific: top row
        for c in range(cols):
            dfs(0, c, pacific)

        # Pacific: left column
        for r in range(rows):
            dfs(r, 0, pacific)

        # Atlantic: bottom row
        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        # Atlantic: right column
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        result = []

        # Cell must be reachable from BOTH oceans
        for r in range(rows):
            for c in range(cols):

                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result