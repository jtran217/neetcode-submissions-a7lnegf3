class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Closest to me means shortest distance -> Min Heap
        # minheap can store tuple, as long as first element is some numerical value
        # Idea is to calculate distance push to tuple in format (distance, [x,y])
        # Pop k amount into some result array.

        min_heap = []
        result = []
        heapq.heapify(min_heap)

        for point in points:
            x,y = point
            d = math.sqrt(x**2 + y**2)
            heapq.heappush(min_heap,(d,[x,y]))
        for i in range(k):
            result.append(heapq.heappop(min_heap)[1])
        return result