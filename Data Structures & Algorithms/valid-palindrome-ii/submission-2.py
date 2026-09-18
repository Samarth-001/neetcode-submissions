class Solution:       

    def validPalindrome(self, s: str) -> bool:

        def check(self, s: str, l: int, r: int) -> bool:

            while l<r:
                if s[l]!=s[r]:
                    return False
                l = l+1
                r = r-1
            return True 
        
        l = 0
        r = len(s) - 1

        while l<r:
            if s[l]!=s[r]:
                return check(self, s, l+1, r) or check(self, s, l, r-1)
            l = l+1
            r = r-1
        
        return True  