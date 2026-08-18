class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [x*-1 for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap) * -1
            y = heapq.heappop(maxHeap) * -1

            if x ==y:
                continue
            left = abs(x-y) * - 1
            heapq.heappush(maxHeap,left)
        
        if len(maxHeap) > 0:
            return maxHeap[0] * - 1
        return 0