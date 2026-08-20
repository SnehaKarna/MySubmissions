class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []
        subset = []

        def dfs(start):

            res.append(subset.copy())  # save current subset

            for i in range(start, len(nums)):

                if i > start and nums[i] == nums[i - 1]:
                    continue             # skip duplicate at same level

                subset.append(nums[i])   # choose
                dfs(i + 1)               # move to next element
                subset.pop()             # backtrack

        dfs(0)

        return res