class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Edge case
        if len(t) > len(s):
            return ""

        # Frequency of characters we need
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        # Frequency of current window
        window = {}

        # Number of unique characters currently satisfied
        have = 0

        # Total unique characters that need to be satisfied
        needCount = len(need)

        left = 0

        # Variables to store the best answer
        resLeft = 0
        resRight = 0
        minLength = float("inf")

        # Expand the window
        for right in range(len(s)):

            # Add current character to window
            window[s[right]] = window.get(s[right], 0) + 1

            # Did we just satisfy one required character?
            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1

            # While current window is valid
            while have == needCount:

                # Update minimum window if current one is smaller
                if (right - left + 1) < minLength:
                    minLength = right - left + 1
                    resLeft = left
                    resRight = right

                # Remove the left character from the window
                window[s[left]] -= 1

                # If removing it makes the window invalid,
                # decrease 'have'
                if (
                    s[left] in need and
                    window[s[left]] < need[s[left]]
                ):
                    have -= 1

                # Remove key if frequency becomes 0
                if window[s[left]] == 0:
                    del window[s[left]]

                # Shrink window
                left += 1

        # No valid window found
        if minLength == float("inf"):
            return ""

        # Return the smallest window
        return s[resLeft:resRight + 1]