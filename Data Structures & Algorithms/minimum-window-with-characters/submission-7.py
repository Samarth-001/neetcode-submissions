class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t)> len(s):
            return ""

        hm1={}
        for ch in t:
            hm1[ch] = hm1.get(ch,0)+1

        formed = 0
        
        hm2={}
        l = 0
        r=0
        ans = ""
        ans_len = len(s) + 1

        while r < (len(s)):
            if s[r] in hm1:
                hm2[s[r]] = hm2.get(s[r],0)+1
            
            if s[r] in hm1 and hm2[s[r]]==hm1[s[r]]:
                formed+=1
            
            while formed == len(hm1):
                if s[l] in hm1:
                    window_len = r-l+1
                    if window_len < ans_len:
                        ans = s[l:r+1]
                        ans_len = window_len
                    hm2[s[l]] -= 1
                    if hm2[s[l]]<hm1[s[l]]:
                        formed-=1
                l+=1
            r+=1
        
        # print(ans)
        if ans == s+t:
            return ""
        
        return ans