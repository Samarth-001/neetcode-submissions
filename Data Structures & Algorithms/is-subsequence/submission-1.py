class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s == "":
            return True
            
        l,r = 0,len(s)

        for ch in t:
            if ch == s[l]:
                l+=1
            if l == r:
                return True
        
        return False