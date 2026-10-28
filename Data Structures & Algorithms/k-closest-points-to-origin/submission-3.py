class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)
        res = []

        for point in points:
            x,y = point

            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(minHeap,(distance,[x,y]))
        
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        
        return res