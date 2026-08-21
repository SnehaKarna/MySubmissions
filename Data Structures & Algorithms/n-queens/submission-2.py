class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []

        # Board: initially all empty
        board = [["."] * n for _ in range(n)]

        def isSafe(row, col):

            # Check column
            for r in range(row):
                if board[r][col] == "Q":
                    return False

            # Check upper-left diagonal
            r = row - 1
            c = col - 1

            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            # Check upper-right diagonal
            r = row - 1
            c = col + 1

            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1

            return True

        def dfs(row):

            # All rows have a queen → solution found
            if row == n:
                solution = []

                for r in board:
                    solution.append("".join(r))

                res.append(solution)
                return

            # Try every column in this row
            for col in range(n):

                # Can't place queen here
                if not isSafe(row, col):
                    continue

                # Choose
                board[row][col] = "Q"

                # Move to next row
                dfs(row + 1)

                # Backtrack
                board[row][col] = "."

        dfs(0)

        return res