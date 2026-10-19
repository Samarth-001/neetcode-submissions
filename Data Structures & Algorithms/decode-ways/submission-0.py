class Solution:
    def numDecodings(self, s: str) -> int:
        hm = {'A':'1', 'B':'2', 'C':'3', 'D':'4', 'E':'5', 'F':'6', 'G':'7', 'H':'8', 'I':'9', 'J':'10', 'K':'11', 'L':'12', 'M':'13', 'N':'14', 'O':'15', 'P':'16', 'Q':'17', 'R':'18', 'S':'19', 'T':'20', 'U':'21', 'V':'22', 'W':'23', 'X':'24', 'Y':'25', 'Z':'26'}

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
