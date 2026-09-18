class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = len(heights) - 1
        ans = 0
        
        i = 0
        while i < l:

            area = (l-i) * min(heights[i], heights[l])
            ans = max(ans, area)

            if heights[i] <= heights[l]:
                i += 1
            else:
                l -= 1
        return ans