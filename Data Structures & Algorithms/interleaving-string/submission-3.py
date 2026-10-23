class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False

        mem = {}

        def find(i,j):
            k = i+j
            if k>len(s3):
                return False

            if i==len(s1) and j==len(s2):
                return True

            if (i,j) in mem:
                return mem[(i,j)]

            ans = False
            if (s3[k] == s1[i:i+1]) and (s3[k] == s2[j:j+1]):
                ans = find(i+1,j) or find(i,j+1)
            elif s3[k] == s1[i:i+1]:
                ans = find(i+1,j)
            elif s3[k] == s2[j:j+1]:
                ans = find(i,j+1)
            
            mem[(i,j)] = ans
            return ans
        
        return find(0,0)