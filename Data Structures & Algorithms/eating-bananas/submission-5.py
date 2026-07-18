class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxBananas = max(piles)
        minEat = maxBananas

        l,r = 1, maxBananas
        while l<=r:
            k = (l + r) // 2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile/k)
            if totalTime <= h:
                r = k - 1
                minEat = min(minEat,k)
            else:
                l = k + 1
        return minEat