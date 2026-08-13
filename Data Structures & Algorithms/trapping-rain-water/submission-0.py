class Solution:
    def trap(self, height: List[int]) -> int:
        # n = len(height)
        # if n == 0:
        #     return 0

        # leftMax = [0] * n
        # rightMax = [0] * n

        # leftMax[0] = height[0]
        # for i in range(1, n):
        #     leftMax[i] = max(leftMax[i - 1], height[i])

        # rightMax[n - 1] = height[n - 1]
        # for i in range(n - 2, -1, -1):
        #     rightMax[i] = max(rightMax[i + 1], height[i])

        # res = 0
        # for i in range(n):
        #     res += min(leftMax[i], rightMax[i]) - height[i]
        # return res
























        left = 0
        right = len(height) -1

        leftMax = height[left]
        rightMax = height[right]


        ans = 0

        while left<right:
            if leftMax < rightMax:
                left += 1

                leftMax = max(leftMax, height[left])

                ans += leftMax - height[left]

            else:

                right -= 1
                rightMax = max(rightMax, height[right])

                ans += rightMax - height[right]

        return ans