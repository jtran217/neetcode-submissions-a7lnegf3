class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mProfit = 0
        l = 0
        r = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l += 1
                continue
            profit = prices[r] - prices[l]
            mProfit = max(mProfit,profit)
            r += 1
        
        return mProfit




