class Solution:
    def trap(self, height: List[int]) -> int:
        
        l=[]
        maxnum = 0
        for i in range(len(height)):
            l.append(maxnum)
            
            maxnum = max(maxnum, height[i])
        
        r=[0]*len(height)
        maxnum = 0
        for i in range(len(height) - 1, -1, -1):
            r[i] = maxnum
            maxnum = max(maxnum, height[i])
    
        maxnum = 0
        for i in range(len(height)):
            calc = min(l[i], r[i]) - height[i]
            if calc > 0:
                maxnum += calc
        return maxnum