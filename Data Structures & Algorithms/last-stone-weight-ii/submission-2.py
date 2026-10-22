class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        mem = {}

        def find(left, right, i):
            if i>=len(stones):
                # print(right-left)
                return abs(right-left)
            
            if (left,right,i) in mem:
                return mem[(left,right,i)] 
            
            mem[(left,right,i)] = min(find(left+stones[i], right, i+1), find(left, right+stones[i], i+1))
            return mem[(left,right,i)]
        
        return find(0,0,0)