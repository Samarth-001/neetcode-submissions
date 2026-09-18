class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        l = []
        prod = 1

        for num in nums:
            l.append(prod)
            prod = prod * num
        
        r = []
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            r.append(prod)
            prod = prod * nums[i]

        result = []
        numlen = len(nums)
        for i in range(numlen):
            # print(i,numlen-i)
            point = l[i]*r[numlen-i-1]
            result.append(point)

        return result