class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minp = prices[0]
        profit = 0

        for price in prices:
            minp = min(minp, price)
            cprofit = price - minp
            profit = max(profit, cprofit)

        return profit