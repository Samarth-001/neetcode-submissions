class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        pass

        hm1 = {}
        hm2 = {}

        for num in target:
            hm1[num] = hm1.get(num,0) + 1
        for num in arr:
            hm2[num] = hm2.get(num,0) + 1
        
        return hm1 == hm2
