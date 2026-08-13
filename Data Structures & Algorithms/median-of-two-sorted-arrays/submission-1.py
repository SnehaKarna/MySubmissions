class Solution:
    def findMedianSortedArrays(self, A, B):

        # 1. Make A the smaller array
        if len(A) > len(B):
            A, B = B, A

        m = len(A)
        n = len(B)

        # 2. Binary search A
        left = 0
        right = m

        half = (m + n + 1) // 2

        while left <= right:

            # 3. Partition A
            i = (left + right) // 2

            # 4. Partition B
            j = half - i

            # 5. Four boundary values
            leftA = A[i - 1] if i > 0 else float("-inf")
            rightA = A[i] if i < m else float("inf")

            leftB = B[j - 1] if j > 0 else float("-inf")
            rightB = B[j] if j < n else float("inf")

            # 6. Correct partition
            if leftA <= rightB and leftB <= rightA:

                maxLeft = max(leftA, leftB)
                minRight = min(rightA, rightB)

                # 7. Odd
                if (m + n) % 2:
                    return maxLeft

                # 8. Even
                return (maxLeft + minRight) / 2

            # 9. Move partition left
            elif leftA > rightB:
                right = i - 1

            # 10. Move partition right
            else:
                left = i + 1