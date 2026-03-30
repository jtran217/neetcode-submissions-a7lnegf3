class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0 
        r = 1
        m_p = 0
        # left is buy
        # right is sell
        # profit = sell - buy
        while r < len(prices):
            if prices[l] > prices[r]:
                l += 1
                r = l + 1
                continue
            profit = prices[r] - prices[l]
            m_p = max(m_p,profit)
            r += 1
        return m_p
            