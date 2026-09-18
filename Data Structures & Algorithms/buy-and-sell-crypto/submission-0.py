class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        if len(prices) < 2:
            return 0
        
        l_m = prices[0]

        for i , val in enumerate(prices):
            profit = prices[i] - l_m
            mp = max(profit, mp)

            l_m = min(prices[i], l_m)

        return mp
