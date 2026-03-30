class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Know h is max hours we can afford
        # max k is largest in group
        # Can binary search, if time <= h, r = m-1 if time > h l = m + 1

        l, r = 1, max(piles)
        res = r

        while l <= r:
            totalTime = 0

            k = (l + r) // 2

            for p in piles:
                totalTime += math.ceil(float(p)/k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
