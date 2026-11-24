class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        pass

        st = []

        for ch in s:
            if st and ch == ")" and st[-1] == "(":
                st.pop()
            else:
                st.append(ch)
        
        return len(st)