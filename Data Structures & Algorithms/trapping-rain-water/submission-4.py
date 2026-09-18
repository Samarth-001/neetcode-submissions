class Solution:
    def trap(self, height: List[int]) -> int:
        
        # l=[0,0,2,2,3,3,3,3,3,3]
        # r=[3,3,3,3,3,3,3,2,1,0]
        # h=[0,2,0,3,1,0,1,3,2,1]
        l=[]
        maxl = 0
        for i in range(len(height)):
            l.append(maxl)
            
            maxl = max(maxl, height[i])
        
        # print(l)

        r=[0]*len(height)
        maxr = 0
        for i in range(len(height) - 1, -1, -1):
            r[i] = maxr
            maxr = max(maxr, height[i])
        
        # print(r)

        area = 0
        for i in range(len(height)):
            calc = min(l[i], r[i]) - height[i]
            if calc > 0:
                area += calc
        return area


        # formula = min(3,3) - 0