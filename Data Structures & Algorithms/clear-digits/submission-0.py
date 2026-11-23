class Solution:
    def clearDigits(self, s: str) -> str:
        pass

        st = []

        for ch in s:
            if ord(ch) >= 48 and ord(ch) <=57:
                st.pop()
            else:
                st.append(ch)
        
        ans = ""
        for ch in st:
            ans+=ch
        
        return ans