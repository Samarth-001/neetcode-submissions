class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        ans = []
        
        while l<=r:
            if abs(nums[l])>=abs(nums[r]):
                ans.append(nums[l]*nums[l])
                l+=1
            else:
                ans.append(nums[r]*nums[r])
                r-=1

        # print(ans)

        l = 0
        r = len(nums)-1
        
        while l<=r:
            temp = ans[l]
            ans[l] = ans[r]
            ans[r] = temp
        
            l+=1
            r-=1
        
        return ans