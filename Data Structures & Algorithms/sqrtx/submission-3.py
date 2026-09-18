class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 1:
            return 1
            
        l = 0
        r = int(x/2)
        mid = 0

        while l<=r:
            mid = int(l+((r-l)/2))
            print(l,mid,r)
            sq = mid*mid
            if sq == x:
                return mid
            elif sq < x:
                l = mid+1
            else:
                r = mid-1
            
        if mid*mid >= x:
            return mid -1
        return mid