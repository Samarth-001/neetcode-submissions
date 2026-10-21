class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        mem = {}

        def find(remaining):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            
            if remaining in mem:
                return mem[remaining]

            count = 0

            for num in nums:
                count+= find(remaining-num)
            
            mem[remaining] = count
            return count
        
        return find(target)
