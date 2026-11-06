class Solution:
    def compress(self, chars: List[str]) -> int:
        
        l = 0
        r = 0
        s = ""
        
        while r < len(chars):
            while r < len(chars) and chars[r] == chars[l]:
                r+=1
            if r-l != 1:
                s = s+ chars[l] + str(r-l)
            else:
                s = s+ chars[l]
            l=r
        
        print(s)
        ans = len(s)
        
        l = 0
        for ch in s:
            chars[l] = ch
            l+=1
        
        return ans