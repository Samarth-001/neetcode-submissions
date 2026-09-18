class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        st = []

        for ch in tokens:

            if ch.lstrip("-").isdigit():
                st.append(int(ch))
            elif ch == '+':
                st.append(st.pop() + st.pop())
            elif ch == '*':
                st.append(st.pop() * st.pop())
            elif(ch == '-'):
                i1=st.pop()
                st.append(st.pop()-i1)
            elif(ch == '/'):
                i1=st.pop()
                st.append(int(st.pop()/i1))

            # print(st)
        
        return int(st.pop())