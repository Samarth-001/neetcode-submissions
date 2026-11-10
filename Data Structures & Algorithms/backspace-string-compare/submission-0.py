class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        pass

        s1 = ""
        count = 0
        r = len(s)-1
        
        while r>-1:
            if s[r] == "#":
                count+=1
            else:
                if count>0:
                    count-=1
                else:
                    s1+=s[r]
            r-=1
        
        s2 = ""
        count = 0
        r = len(t)-1
        
        while r>-1:
            if t[r] == "#":
                count+=1
            else:
                if count>0:
                    count-=1
                else:
                    s2+=t[r]
            r-=1
        
        # print(s2)
        return s1==s2
                    