class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pass

        potions.sort()
        
        output = []

        for spell in spells:

            l,r = 0,len(potions) 
            ans = len(potions)

            while l<=r:
                mid = int(l+((r-l)/2))

                if mid<=(len(potions)-1) and (spell*potions[mid])>=success:
                    ans = mid
                    r = mid-1
                else:
                    l = mid+1
            
            output.append(len(potions)-ans)
            
        return output