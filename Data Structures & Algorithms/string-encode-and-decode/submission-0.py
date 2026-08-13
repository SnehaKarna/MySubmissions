class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for num in strs:
            l = len(num)
            s += str(l) + "#" + num

        return s

    def decode(self, s: str) -> List[str]:
        ans= []
        i=0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1;
            
            length = int(s[i:j])

            word = s[j+1 : j+1+length]

            ans.append(word)

            i = j + 1 + length

        return ans

