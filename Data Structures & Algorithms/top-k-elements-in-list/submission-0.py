class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = dict()
        for i in nums:
             mp[i] = mp.get(i, 0) + 1

        arr = sorted(mp.items(), key = lambda x:x[1], reverse = True)

        ans = []

        for num, freq in arr[:k]:
            ans.append(num)

        return ans






  