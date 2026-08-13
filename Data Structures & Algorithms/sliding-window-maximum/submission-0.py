class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        ans = []

        # Move the left pointer from 0 to the last possible window
        for left in range(len(nums) - k + 1):

            # Maximum of the current window
            maxElement = nums[left]

            # Check the remaining elements in the window
            for i in range(left, left + k):
                maxElement = max(maxElement, nums[i])

            # Store the maximum
            ans.append(maxElement)

        return ans