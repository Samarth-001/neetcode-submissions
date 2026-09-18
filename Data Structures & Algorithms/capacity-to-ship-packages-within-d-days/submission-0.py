class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def calc(num, weights, days):
            
            count=0
            for w in weights:
                count+=w
                if count<=num:
                    continue
                days-=1
                count = w
            
            if count!=0:
                days-=1
            
            if days<0:
                return -1
            return 1
        

        l = max(weights)
        r = sum(weights)
        ans = r
        
        while l<=r:
            mid = int(l+((r-l)/2))

            cal = calc(mid, weights, days)
            if cal==1:
                ans = min(ans, mid)
                r = mid-1
            else:
                l = mid+1
        
        # print(ans)
        return ans