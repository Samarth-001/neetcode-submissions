class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        area = 0

        for i in range(len(heights)):
            if not st:
                st.append([heights[i], i])
            else:
                while st and st[-1][0] >= heights[i]:
                    height, index = st.pop()
                    left = st[-1][1] if st else -1
                    area = max(area, (i - left - 1) * height)

                st.append([heights[i], i])

        while st:
            height, index = st.pop()
            left = st[-1][1] if st else -1
            width = len(heights) - left - 1
            area = max(area, width * height)

        return area