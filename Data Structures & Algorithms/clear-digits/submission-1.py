class Solution:
    def clearDigits(self, s: str) -> str:
        pass

        st = []

        for ch in s:
            if ord(ch) >= 48 and ord(ch) <=57:
                st.pop()
            else:
                st.append(ch)
        
        return "".join(st)