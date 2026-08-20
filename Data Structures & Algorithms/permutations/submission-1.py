class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []
        used = [False] * len(nums)

        def dfs():

            # We used every number → one permutation is complete
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            # Try every number
            for i in range(len(nums)):

                # Already used → skip
                if used[i]:
                    continue

                # Choose
                subset.append(nums[i])
                used[i] = True

                # Build the remaining positions
                dfs()

                # Backtrack
                subset.pop()
                used[i] = False

        dfs()

        return res