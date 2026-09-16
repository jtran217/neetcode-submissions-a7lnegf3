class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #  know max k = max array
        # if k < minK seen and total h < h replace

        l,r = 1, max(piles)
        minK = max(piles)
        while l<=r:
            k = (l+r)//2
            # Bananna/k round up
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile)/k)
            if totalTime  <=h:
                minK = k
                r = k -1
            else:
                l = k +  1
        
        return minK

            
