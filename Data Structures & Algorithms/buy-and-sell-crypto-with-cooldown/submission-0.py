class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mem = {}

        def find(i,status):
            if i>=len(prices):
                return 0

            if (i,status) in mem:
                return mem[(i,status)]    
            
            if status == "buy":
                mem[(i,status)] = max(find(i+1, "sell")-prices[i],find(i+1, "buy"))
            else:
                mem[(i,status)] = max(find(i+2,"buy")+prices[i],find(i+1,"sell"))
            
            return mem[(i,status)]
            
        return find(0,"buy")
