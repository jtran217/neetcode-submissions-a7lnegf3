class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [stone * -1 for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = heapq.heappop(maxHeap) * -1
            x = heapq.heappop(maxHeap) * -1
            if x == y:
                continue
            newWeight = (y-x) * -1
            heapq.heappush(maxHeap,newWeight)
        
        if maxHeap:
            return maxHeap[0] * -1
        else:
            return 0