import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for x, y in points:

            # Squared distance from origin
            dist = x * x + y * y

            # Negative distance → simulate Max Heap
            heapq.heappush(heap, (-dist, x, y))

            # Keep only K closest points
            if len(heap) > k:
                heapq.heappop(heap)

        # Extract points from heap
        return [[x, y] for dist, x, y in heap]