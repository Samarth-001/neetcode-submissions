class Solution:
    def numDecodings(self, s: str) -> int:

        mem = {}

        def find(i):
            if i == len(s):
                return 1

            if s[i] == '0':
                return 0
            
            if i in mem:
                return mem[i]
            
            ways = find(i + 1)

            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                ways += find(i + 2)
            
            mem[i] = ways

            return mem[i]

        return find(0)
