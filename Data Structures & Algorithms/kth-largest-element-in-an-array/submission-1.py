class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-x for x in nums]
        heapq.heapify(maxHeap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(maxHeap))
        return res[-1] * -1