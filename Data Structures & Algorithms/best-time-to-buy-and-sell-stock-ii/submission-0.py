class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mp = 0
        ans = 0
        minp = prices[0]
        for price in prices:
            
            if price <= minp:
                minp = price
            
            profit = price-minp
            if profit< mp:
                print(minp, price, mp)
                ans+=mp
                mp = 0
                minp = price
            else:
                mp = profit
        ans+=mp
        return ans