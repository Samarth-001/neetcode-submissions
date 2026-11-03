class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        i = 0
        j = 0

        while i<len(t) and j<len(s):
            if t[i] == s[j]:
                i+=1
                j+=1
            else:
                j+=1

        print(i,j)
        if i==len(t):
            return 0
        return (len(t)-i)

        # while i <= len(t)-1 and t[i] == s[i]:
        #     i+=1
        
        # if len(t) == i:
        #     return 0
        
        # return len(t)-i