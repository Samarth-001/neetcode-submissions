class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zp = 0
        tp = len(nums)-1
        
        i=0

        while i<=tp:
            if nums[i]==0:
                temp = nums[i]
                nums[i] = nums[zp]
                nums[zp] = temp
                zp += 1
                i+=1
            
            elif nums[i]==2:
                temp = nums[i]
                nums[i] = nums[tp]
                nums[tp] = temp
                tp -= 1
            else:  
                i+=1