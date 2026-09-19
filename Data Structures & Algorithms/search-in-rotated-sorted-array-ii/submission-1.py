class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l=0
        r=len(nums)-1

        while(l<r):

            mid = int(l+((r-l)/2))

            # print(nums[l], nums[mid], nums[r])
            if nums[mid]==nums[l] and nums[l] == nums[r]:
                l+=1
                r-=1
            elif nums[mid]>=nums[l]:
                l = mid+1
            else:
                r = mid
            
        # while l>0 and (nums[l] == nums[l-1]):
        #     l-= 1
        
        print(l)

        if target>=nums[l] and target<=nums[-1]:
            r=len(nums)-1
        else:
            r=l
            l=0
        
        while(l<=r):
            mid = int(l+((r-l)/2))
            
            if nums[mid]==target:
                return True
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1

        return False

























