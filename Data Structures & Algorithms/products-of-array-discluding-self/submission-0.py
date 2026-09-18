class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre = [0] * l
        suf = [0] * l
        pre_multiple = 1        
        for i, num in enumerate(nums):
            pre[i] = pre_multiple
            pre_multiple = pre_multiple * nums[i]
        
        print(pre)
            
        suf_multiple = 1        
        for i, num in enumerate(nums):
            suf[i] = suf_multiple
            suf_multiple = suf_multiple * nums[l-i-1]
            
            suf_multiple
        
        print(suf)
        result = []
        for i, num in enumerate(pre):
            result.append(num*suf[l-i-1])
        return result
        
    #     [1,2,4,6]

    # pre [0,1,2,8]
    # suf [48,24,6,0]
    
    # ans [48,24,12,8]
        
        
    #     [-1,0,1,2,3]

    # pre [1,-1,0,0,0]
    # suf [0,6,6,3,1]
    
    # ans [48,24,12,8]