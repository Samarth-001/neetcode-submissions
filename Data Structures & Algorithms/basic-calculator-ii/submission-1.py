class Solution:
    def calculate(self, s: str) -> int:

        st = []
        prev_op = "+"
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
                continue
            if ch == " ":
                continue

            if prev_op == "+":
                st.append(num)
            elif prev_op == "-":
                st.append(-num)
            elif prev_op == "*":
                val = st.pop()
                st.append(val * num)
            else:
                val = st.pop()
                st.append(int(val / num))

            prev_op = ch
            num = 0

        if prev_op == "+":
            st.append(num)
        elif prev_op == "-":
            st.append(-num)
        elif prev_op == "*":
            st.append(st.pop() * num)
        else:
            val = st.pop()
            st.append(int(val / num))

        return sum(st)