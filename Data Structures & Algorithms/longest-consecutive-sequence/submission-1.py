class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maxlength = 0

        for i in nums:
            if i-1 in numSet:
                continue
            else:

                current = i
                length = 1
               

                while current+1 in numSet:
                    current += 1
                    length += 1

                maxlength = max(maxlength, length)
        

        return maxlength