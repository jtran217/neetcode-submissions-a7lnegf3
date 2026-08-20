class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mapping = defaultdict(list)
        minHeap = []
        heapq.heapify(minHeap)

        for point in points:
            x,y = point[0],point[1]
            distance = math.sqrt(x**2 + y**2)
            mapping[distance].append(point)
            heapq.heappush(minHeap,distance)
        res = []
        for i in range(k):
            distance = heapq.heappop(minHeap)
            res.append(mapping[distance].pop())
        return res 

        
        