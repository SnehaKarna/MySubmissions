import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Python heapq is Min Heap
        # Use negative values to simulate Max Heap
        heap = [-stone for stone in stones]

        heapq.heapify(heap)

        while len(heap) > 1:

            # Get two largest stones
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            # If they are different, push remaining stone
            if first != second:
                heapq.heappush(heap, -(first - second))

        # If no stone remains → 0
        # Otherwise return the remaining stone
        return -heap[0] if heap else 0