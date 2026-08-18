import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for num in nums:

            # Add current number
            heapq.heappush(heap, num)

            # Keep only K largest numbers
            if len(heap) > k:
                heapq.heappop(heap)

        # Smallest among K largest = Kth largest
        return heap[0]