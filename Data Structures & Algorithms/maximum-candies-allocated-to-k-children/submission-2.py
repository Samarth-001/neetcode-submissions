class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        l, r = 1, max(candies)
        ans = 0

        while l <= r:
            mid = l + (r - l) // 2

            children = 0

            for candy in candies:
                children += candy // mid

            if children >= k:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans