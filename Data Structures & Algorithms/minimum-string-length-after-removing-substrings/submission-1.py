class Solution:
    def minLength(self, s: str) -> int:
        pass

        st = []

        for ch in s:
            if not st:
                st.append(ch)
                continue
            
            if (st[-1] == 'A' and ch == "B") or (st[-1] == 'C' and ch == "D"):
                st.pop()
                continue
            
            st.append(ch)

        return len(st)