class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):

            # Found the complete word
            if index == len(word):
                return True

            # Outside grid
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # Wrong letter or already visited
            if board[r][c] != word[index]:
                return False

            # Mark as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Try all 4 directions
            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            # Backtrack: restore the cell
            board[r][c] = temp

            return found

        # Try every cell as a starting point
        for r in range(rows):
            for c in range(cols):

                if dfs(r, c, 0):
                    return True

        return False