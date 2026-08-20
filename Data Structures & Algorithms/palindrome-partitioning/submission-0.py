class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        current = []

        def dfs(start):

            # Reached the end → one valid partition
            if start == len(s):
                res.append(current.copy())
                return

            # Try every possible substring
            for end in range(start, len(s)):

                substring = s[start:end + 1]

                # Skip if it is not a palindrome
                if substring != substring[::-1]:
                    continue

                # Choose
                current.append(substring)

                # Continue from the next character
                dfs(end + 1)

                # Backtrack
                current.pop()

        dfs(0)

        return res