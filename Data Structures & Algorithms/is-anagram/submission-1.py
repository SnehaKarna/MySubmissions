class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        mp = dict()

        for ch in s:
            mp[ch] = mp.get(ch, 0) + 1
        
        for ch in t:
            if ch not in mp:
                return False
            else:
                mp[ch] -= 1
            
            if mp[ch] < 0:
               return False
      
        return True
          
        
        
        
        