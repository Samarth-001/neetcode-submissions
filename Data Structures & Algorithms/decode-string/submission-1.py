class Solution:
    def decodeString(self, s: str) -> str:
        
        def ans(s, k, i):
            f = ""
            while i<len(s) and s[i]!="]":
                if not s[i].isdigit():
                    f+=s[i]
                    i+=1
                else: 
                    dig = ""
                    while(s[i]!="["):
                        dig += s[i]
                        i+=1
                    print(dig)
                    t,i=ans(s, int(dig), i+1)
                    f+=t
            print(f)
            return f*k, i+1
    
        hel,i= ans(s, 1, 0)
        return hel