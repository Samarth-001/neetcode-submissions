class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def calc(r, piles, h):
            # print(piles, r)
            for num in piles:
                # print(h)
                h -= int(math.ceil(num/r))
            
            if h>0:
                return 1
            elif h == 0:
                return 0
            return -1
        
        r = 0
        for num in piles:
            r = max(num,r)

        l = 1
        ans = r
        print(l,r)
        while l<=r:
            mid = int(l + (r-l)/2)

            cal = calc(mid, piles, h)
            if cal == 0 or cal == 1:
                ans = min(ans, mid)
                r = mid-1
            else:
                l=mid+1
        
        # print(ans)
        return ans
