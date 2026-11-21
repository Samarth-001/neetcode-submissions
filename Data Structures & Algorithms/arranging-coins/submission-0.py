class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        l,r=0,n
        ans = 0

        while l<=r:
            mid = int(l+(r-l)/2)
            
            target = (mid*(mid+1))/2

            if target<=n:
                print(l,r,mid)
                ans = max(ans,mid)
                l = mid+1
            else:
                r = mid-1

        return ans