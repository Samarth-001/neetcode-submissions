class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        r = len(numbers)-1

        l = 0

        while(r>l):
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r = r-1
            else:
                l = l+1
        
        return [numbers[l], numbers[r]]