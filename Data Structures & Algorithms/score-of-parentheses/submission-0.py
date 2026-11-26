class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = [0]

        for ch in s:
            if ch == "(":
                st.append(0)
            else:
                inner = st.pop()

                if inner == 0:
                    st.append(st.pop() + 1)
                else:
                    st.append(st.pop() + (inner * 2))

        return st[0]