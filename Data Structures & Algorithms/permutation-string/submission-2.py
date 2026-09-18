class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        hm={}
        for ch in s1:
            hm[ch] = hm.get(ch,0)+1
        
        l=0
        r=0
        print(hm)
        print(" ")
        hm1={}
        while r<len(s2):
            if r>=len(s1):
                hm1[s2[l]]-=1
                if hm1[s2[l]] == 0:
                    hm1.pop(s2[l])
                l+=1
            hm1[s2[r]] = hm1.get(s2[r],0)+1

            print(hm1)
            if hm == hm1:
                return True

            r+=1
        return False
