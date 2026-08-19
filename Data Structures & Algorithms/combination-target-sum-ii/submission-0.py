class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()   # Put duplicates next to each other
        res = []
        subset = []

        def dfs(start, total):

            # We found a valid combination
            if total == target:
                res.append(subset.copy())
                return

            # Sum became too large
            if total > target:
                return

            for i in range(start, len(candidates)):

                # Skip duplicate values at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Choose current number
                subset.append(candidates[i])

                # i + 1 because each element can be used only once
                dfs(i + 1, total + candidates[i])

                # Backtrack: remove the number we just chose
                subset.pop()

        dfs(0, 0)

        return res