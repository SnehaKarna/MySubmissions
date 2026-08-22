class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):

            # Outside grid
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Not an O
            if board[r][c] != "O":
                return

            board[r][c] = "T"     # Mark O as safe

            dfs(r + 1, c)         # Down
            dfs(r - 1, c)         # Up
            dfs(r, c + 1)         # Right
            dfs(r, c - 1)         # Left

        # Check top and bottom borders
        for c in range(cols):

            if board[0][c] == "O":
                dfs(0, c)

            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        # Check left and right borders
        for r in range(rows):

            if board[r][0] == "O":
                dfs(r, 0)

            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)

        # Convert the board
        for r in range(rows):
            for c in range(cols):

                if board[r][c] == "O":
                    board[r][c] = "X"    # Surrounded

                elif board[r][c] == "T":
                    board[r][c] = "O"    # Safe