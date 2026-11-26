class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        if k == len(num):
            return "0"

        st = []
        re = 0

        for ch in num:

            while st and re < k and ch < st[-1]:
                st.pop()
                re += 1

            st.append(ch)

        while re < k:
            st.pop()
            re += 1

        result = "".join(st).lstrip("0")

        return result or "0"