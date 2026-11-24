class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        st = []

        for ch in s:
            if not st or st[-1][0]!=ch:
                st.append([ch,1])
                continue
            
            if st[-1][1] != (k-1):
                pch, val = st.pop()
                st.append([pch,val+1])
            else:
                st.pop()

        ans = ""
        for ch,val in st:
            while val!=0:
                ans+=ch
                val-=1
        return ans