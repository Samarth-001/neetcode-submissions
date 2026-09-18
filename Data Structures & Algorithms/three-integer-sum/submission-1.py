class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    

        l = len(nums) - 1
        
        if l<2:
            return []

        result = []

        nums.sort()

        for p in range(len(nums) - 2):

            if p > 0 and nums[p] == nums[p - 1]:
                continue

            q = p + 1
            r = len(nums) - 1

            while q < r:

                total = nums[p] + nums[q] + nums[r]

                if total == 0:
                    result.append([nums[p], nums[q], nums[r]])

                    q += 1
                    r -= 1

                    while q < r and nums[q] == nums[q - 1]:
                        q += 1

                    while q < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif total < 0:
                    q += 1

                else:
                    r -= 1
                
        
        return result

