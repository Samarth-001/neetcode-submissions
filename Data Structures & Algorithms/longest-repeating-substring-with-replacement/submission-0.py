class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        ans = 0
        le = len(s)
        if le == 1:
            return 1

        r=0
        l=0
        
        hm = {}
        mf = 0
        while (l<=r and r<le):
            if s[r] not in hm:
                hm[s[r]] = 1
            else:
                hm[s[r]] += 1

            mf = max(mf, hm[s[r]])

            print(mf)

            if (((r-l+1)-mf) > k):
                hm[s[l]] -= 1
                l += 1
            
            ans = max(ans, (r-l+1))
            
            r += 1
        
        return ans