class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Want either last stone weight or 0 if none 
        # Each step choose two heaviest -> Max heap? -> Insert -values
        #  x== y then pop both
        #  x < y pop x and y = y-x then add back to heap.
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones) * -1 # Get back to positive value
            y = heapq.heappop(stones) * -1

            if (x == y):
                continue
            elif (x < y):
                y = y-x
                heapq.heappush(stones,-y)
            else:
                x = x - y
                heapq.heappush(stones, -x)
        
        return stones[0] * -1 if stones else 0

