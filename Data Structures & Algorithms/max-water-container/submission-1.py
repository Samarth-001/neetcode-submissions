class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # arr = [1,7,2,5,4,7,3,6]
        #       [0,1,2,3,4,5,6,7]
        maxarea = 0
        l = 0
        r = len(heights)-1

        while l<r:
            area = min(heights[l], heights[r]) * (r-l)
            maxarea =  max(maxarea, area)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        
        return maxarea