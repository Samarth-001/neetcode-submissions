class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 1:
            return 1
        hm = set()
        l = 0
        r = 0
        length=0
        ml=0
        while l<=r and r<len(s):
            # print(hm, length)
            if s[r] not in hm:
                hm.add(s[r])
                length+=1
                ml = max(length,ml)
                r+=1
                continue
            while(s[r] in hm):
                hm.remove(s[l])
                l+=1
                length-=1
            
        return ml