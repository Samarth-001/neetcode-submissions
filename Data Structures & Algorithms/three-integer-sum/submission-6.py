class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums = sorted(nums)
        print(nums)

        for i in range(len(nums)-2):
            k = len(nums)-1
            j = i+1
            
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            while j<k:
                calc = nums[j] + nums[k]
                if calc == -nums[i]:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1

                    while j<k and nums[j] == nums[j-1]:
                        j+=1                    
                    k-=1
                    while k>j and nums[k] == nums[k+1]:
                        k-=1
                elif calc < -nums[i]:
                    j+=1
                else:
                    k-=1


        return ans
