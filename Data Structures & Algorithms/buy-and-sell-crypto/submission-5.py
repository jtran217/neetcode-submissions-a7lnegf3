class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l = buy r = selling
        # What condition do we adjust the window? -> When l > r

        l = r =0
        mProfit = 0
        while r < len(prices):
            if (prices[l] > prices[r]):
                l += 1
                continue
            mProfit = max(mProfit, prices[r] - prices[l])
            r += 1
        return mProfit