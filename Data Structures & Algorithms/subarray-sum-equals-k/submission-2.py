class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hm = {0: 1}
        sum = 0
        ans = 0
        i=0

        for num in nums:
            sum+=num
            if sum-k in hm:
                print(num)
                ans+=hm.get((sum-k), 1)
            hm[sum] = hm.get(sum,0) + 1
            i+=1

        return ans


        [2,1,2,4]
        [4,8,12,16,20,24]