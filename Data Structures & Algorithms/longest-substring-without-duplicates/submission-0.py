class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left =0
        maxlength = 0

        cset = set()

        for right in range(len(s)):

            while s[right] in cset:

                cset.remove(s[left])
                left += 1

            cset.add(s[right])

            maxlength = max(maxlength, right - left + 1)
        

        return maxlength