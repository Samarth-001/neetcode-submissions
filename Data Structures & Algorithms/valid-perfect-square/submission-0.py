class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        l,r = 0,num

        while l<=r:
            mid = int(l+(r-l)/2)
            # print(mid)

            target = mid*mid
            
            if target == num:
                return True
            elif target<num:
                l = mid+1
            else:
                r = mid-1

        return False