class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        # [2,4,10,1,5]
        # 2
        # 16

        def isValid(mid, nums, k):
            # print("mid:", mid)
            k-=1
            numSum=0
            for num in nums:
                # print(numSum, num, k)
                numSum+=num
                if numSum>mid:
                    numSum=num
                    k-=1
            
            if k<0:
                # print("False")
                return False
            # print("True")
            return True



        l = max(nums)
        r = sum(nums)

        ans = r

        while l<=r:
            mid = int(l + ((r-l)/2))
            # print((l,mid,r), ans)
            if not isValid(mid, nums, k):
                l=mid+1
            else:
                ans=min(mid,ans)
                r=mid-1
        
        # print(ans)
        return ans