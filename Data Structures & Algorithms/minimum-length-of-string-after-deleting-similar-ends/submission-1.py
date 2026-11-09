class Solution:
    def minimumLength(self, s: str) -> int:
        pass

        if len(s) == 1:
            return 1
        
        l = 0
        r = len(s)-1

        while l<r:
            print(l,r)
            if s[l] == s[r]:
                ch = s[l]
                while l<len(s) and l<r and s[l]==ch:
                    l+=1
                while r>-1 and l<=r and s[r]==ch:
                    r-=1
            else:
                return ((r-l)+1)
        print(l,r)
        
        return ((r-l)+1)
        