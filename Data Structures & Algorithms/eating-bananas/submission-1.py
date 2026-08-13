class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # speed =1

        # while True:
        #     totalTime = 0
        #     for pile in piles:
        #         totalTime += math.ceil(pile/speed)

        #     if totalTime <= h:
        #         return speed
        #     speed += 1
        # return speed


        low = 1
        high = max(piles)

        while low<high:

            mid = (low + high)// 2
            hours = 0


            for pile in piles:
                hours += (pile + mid - 1)// mid


            if hours <= h:
                high = mid
            else:
                low = mid + 1
            
        return low
