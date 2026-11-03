class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        hm = {}
        ans = ""

        for i in s:
            hm[i] = hm.get(i,0) + 1

        print(hm)
        
        for i in order:
            if i in hm:
                for j in range(hm[i]):
                    ans+=i
                v = hm.pop(i)
                        
        for key, value in hm.items():
            print(key, value)
            for i in range(value):
                ans+=key
        return ans
        
