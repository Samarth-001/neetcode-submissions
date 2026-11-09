class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        p = 0
        n = 0

        while nums[p]<0:
            p+=1
        while nums[n]>0:
            n+=1

        while len(ans)!=len(nums):
            
            ans.append(nums[p])
            p+=1
            ans.append(nums[n])
            n+=1

            while p<len(nums) and nums[p]<0:
                p+=1
            while n<len(nums) and nums[n]>0:
                n+=1

        return ans