class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0

        for i in range(len(s)-1):
            
            k = l = i

            while (k>=0 and l<len(s)) and s[k] == s[l]:
                count+=1
                k-=1
                l+=1
            
            k = i
            l = i+1

            while (k>=0 and l<len(s)) and s[k] == s[l]:
                count+=1
                k-=1
                l+=1
        
        return count+1