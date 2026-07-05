import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = {}

        for num in nums:
            if num not in freqCount:
                freqCount[num] = 0
            freqCount[num] += 1
        
        minHeap = []
        heapq.heapify(minHeap)

        for num,freq in freqCount.items():
            heapq.heappush(minHeap,(freq,num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        
        for item in minHeap:
            res.append(item[1])
        return res
        