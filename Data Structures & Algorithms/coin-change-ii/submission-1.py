class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        mem = {}

        def find(remaining, j):
            if remaining == 0:
                return 1
            if remaining <= 0:
                return 0
            
            if (j,remaining) in mem:
                return mem[(j,remaining)]

            count = 0
            for i in range(j, len(coins)):
                if coins[i]<=remaining:
                    count += find(remaining-coins[i], i)
            
            mem[(j,remaining)] = count
            return count

        return find(amount, 0)