class Solution:
    def tribonacci(self, n: int) -> int:
        
        mem = {}
        
        def find(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i == 2:
                return 1
            
            if i in mem:
                return mem[i]

            mem[i] = find(i-1)+find(i-2)+find(i-3)
            return mem[i]

        return find(n)