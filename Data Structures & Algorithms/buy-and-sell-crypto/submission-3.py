class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two pointers -> Sliding window
        # l = buy r = sell
        # p = sell - buy
        # Main idea is finding what condition to adjust the window -> if buying is higher than selling

        l,r = 0,0
        maxP = 0
        for r in range(len(prices)):
            while prices[l] > prices[r]:
                l += 1
                continue
            profit = prices[r] - prices[l]
            maxP = max(maxP,profit)
        return maxP
        