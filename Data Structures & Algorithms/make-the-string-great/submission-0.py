class Solution:
    def makeGood(self, s: str) -> str:
        pass

        st = []

        for ch in s:
            if not st:
                st.append(ch)
                continue
            if abs(ord(st[-1])-ord(ch))==32:
                st.pop()
                continue
            st.append(ch)
        
        ans = ""
        
        for ch in st:
            ans+=ch

        return ans