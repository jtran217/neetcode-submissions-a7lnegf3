class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)
        for i in points:
            x,y = i
            distance = math.sqrt(x**2 +y**2)
            heapq.heappush(minHeap,[distance,x,y])
        res = []
        for i in range(k):
            point = heapq.heappop(minHeap)
            res.append([point[1],point[2]])
        return res