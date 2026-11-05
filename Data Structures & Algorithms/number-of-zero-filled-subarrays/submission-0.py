class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zcount = 0
        ans = 0
        for i in range(-1,len(nums)-1):
            if nums[i+1] == 0:
                zcount +=1
            else:
                while zcount != 0:
                    ans+=zcount
                    zcount-=1

        while zcount != 0:
            ans+=zcount
            zcount-=1
            

        return ans
