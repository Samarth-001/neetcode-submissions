class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []

        nums =sorted(nums)
        print(nums)
        if len(nums)<4:
            print("less than 4")
        else:
            for i in range(len(nums)-3):
                if i>0 and nums[i]==nums[i-1]:
                    continue

                for j in range(i+1, len(nums)-2):
                    if j>i+1 and nums[j]==nums[j-1]:
                        continue

                    l=j+1
                    r= len(nums)-1
                    while l<r:
                        calc = nums[i] + nums[j] + nums[l] + nums[r]
                        if calc == target:
                            ans.append([nums[i],nums[j],nums[l],nums[r]])
                            left_val = nums[l]
                            right_val = nums[r]

                            while l < r and nums[l] == left_val:
                                l += 1

                            while l < r and nums[r] == right_val:
                                r -= 1
                        elif (calc>target):
                            r-=1
                        else:
                            l+=1
        
        return ans

            

        

        # [-3, 0, 1, 2, 3, 3]             [-1, -1, -1, 1, 1, 1]