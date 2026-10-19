class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        mem = {}

        def find(remaining):

            if remaining == 0:
                return 0
            
            if remaining in mem:
                return mem[remaining]

            min_coins = float('inf')

            for coin in coins:
                if coin<=remaining:
                    result = find(remaining - coin)
                    
                    if result != float('inf'):
                        min_coins = min(min_coins, 1+result)
            
            mem[remaining] = min_coins
            return min_coins
        
        result = find(amount)

        return -1 if result == float('inf') else result