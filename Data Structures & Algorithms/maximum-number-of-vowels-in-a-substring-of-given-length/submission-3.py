class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        pass

        l, r = 0, 0
        ans = 0
        count = 0

        while r<len(s):
            # print(l,r)
            if s[r] in ['a','e','i','o','u']:
                count+=1
            if r-l>=k-1:
                # print("inside")
                ans = max(ans, count)

                if s[l] in ['a','e','i','o','u']:
                    count-=1
                l+=1
            
            r+=1
        
        return ans