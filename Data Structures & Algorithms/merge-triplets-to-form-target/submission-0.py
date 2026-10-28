class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        i = j = k = 0
        for triplet in triplets:
            
            if (target[0]<triplet[0] or target[1]<triplet[1] or target[2]<triplet[2]):
                continue
            
            if triplet[0] == target[0]:
                i = 1
            if triplet[1] == target[1]:
                j = 1
            if triplet[2] == target[2]:
                k = 1
        
        if i == 1 and j == 1 and k == 1:
            return True
        
        return False