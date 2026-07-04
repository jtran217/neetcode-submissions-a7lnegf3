import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countSet = {}
        for num in nums:
            if num not in countSet:
                countSet[num] = 0
            countSet[num] += 1
        minHeap = []
        heapq.heapify(minHeap)

        for key,freq in countSet.items():
            heapq.heappush(minHeap,(freq,key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        result = []
        for tup in minHeap:
            result.append(tup[1])
        return result
