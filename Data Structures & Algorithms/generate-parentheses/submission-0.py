class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        current = []

        def dfs(open, close):

            # We used all parentheses → valid combination
            if open == n and close == n:
                res.append("".join(current))
                return

            # We can add '(' if we haven't used n opening brackets
            if open < n:
                current.append("(")
                dfs(open + 1, close)
                current.pop()          # backtrack

            # We can add ')' only if there is an unmatched '('
            if close < open:
                current.append(")")
                dfs(open, close + 1)
                current.pop()          # backtrack

        dfs(0, 0)

        return res