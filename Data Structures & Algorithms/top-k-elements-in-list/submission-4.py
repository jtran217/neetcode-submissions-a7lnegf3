class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = {}

        for num in nums:
            if num not in freqCount:
                freqCount[num] = 0
            freqCount[num] += 1
        
        res = []
        heapq.heapify(res)

        for key,count in freqCount.items():
            heapq.heappush(res,(count*-1,key))
        
        realRes = []
        for i in range(k):
            item = heapq.heappop(res)
            realRes.append(item[1])
        
        return realRes
