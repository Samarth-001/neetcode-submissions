class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = len(height)
        r=l-1
        l_max = [0] * l
        r_max = [0] * l

        l_m = 0

        for i in range(1, l):
            l_max[i] = max(l_m, height[i - 1])
            l_m = max(l_m, height[i-1])
            
        r_m = 0

        for i in range(l - 2, -1, -1):
            r_max[i] = max(r_m, height[i + 1])
            r_m = max(r_m, height[i+1])
        
        area = 0
        for i, val in enumerate(height):
            water = min(l_max[i], r_max[i]) - height[i]
            area += max(0, water)

        return area









