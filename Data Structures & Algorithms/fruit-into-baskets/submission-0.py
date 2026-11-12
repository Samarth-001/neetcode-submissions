class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        if len(fruits) == 1:
            return 1

        ans = 0
        l,r = 0,0
        
        hm = {}

        while r<len(fruits):
            if len(hm)<2:
                hm[fruits[r]] = r
                ans = max(ans, (r-l)+1)
                r+=1
                continue
            
            if fruits[r] not in hm:
                fruit_to_remove = min(hm, key=hm.get)
                l = hm[fruit_to_remove] + 1
                del hm[fruit_to_remove]

            hm[fruits[r]] = r
            ans = max(ans, (r-l)+1)
            r+=1

        return ans