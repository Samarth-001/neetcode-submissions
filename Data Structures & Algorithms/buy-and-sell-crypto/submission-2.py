class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minp = prices[0]
        profit = 0
        
        for price in prices:
            profit = max(profit, (price - minp))
            minp = min(price, minp)

        return profit