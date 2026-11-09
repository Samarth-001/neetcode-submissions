class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort(reverse = True)
        s.sort(reverse = True)
        
        l=0
        r=0
        ans = 0

        while l<len(g) and r<len(s):
            if s[r]>=g[l]:
                l+=1
                r+=1
                ans+=1
            elif s[r]<g[l]:
                l+=1
        
        return ans