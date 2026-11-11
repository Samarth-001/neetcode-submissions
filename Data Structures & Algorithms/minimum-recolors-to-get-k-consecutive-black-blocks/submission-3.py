class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        # if k == 1:
        #     return 1 

        wCount = 0
        l,r = 0,0
        ans = len(blocks)

        while r<len(blocks):
            block = blocks[r]

            if block == 'W':
                wCount += 1
        
            if (r-l) > k-1:
                lblock = blocks[l]
                if lblock == 'W':
                    wCount -= 1
                l+=1
                
                ans = min(ans, wCount)
            
            r+=1
        
        ans = min(ans, wCount)
        
        return ans