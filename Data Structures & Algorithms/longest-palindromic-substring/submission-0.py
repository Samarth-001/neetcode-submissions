class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s)<=1:
            return s
        
        resLen = 0
        start = 0

        for i in range(len(s)-1):

            k = l = i
            
            while (k>=0 and l<len(s)) and s[k]==s[l]:
                k-=1
                l+=1
            
            if resLen < (l-k):
                resLen = l-k-1
                start = k+1
            
            k = i
            l = i+1
            
            while (k>=0 and l<len(s)) and s[k]==s[l]:
                k-=1
                l+=1
            
            if resLen < (l-k):
                resLen = l-k-1
                start = k+1
            
        # print(resLen)
        # print(start)
        # print(s[start:start+resLen])
        return s[start:start+resLen]
    