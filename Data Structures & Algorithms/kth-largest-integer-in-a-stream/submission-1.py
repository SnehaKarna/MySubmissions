import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        # Keep only the k largest elements
        for num in nums:
            heapq.heappush(self.heap, num)

            if len(self.heap) > self.k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:

        # Add new number
        heapq.heappush(self.heap, val)

        # If more than k elements, remove smallest
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # Smallest among k largest = kth largest
        return self.heap[0]