class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pass

        i,j=0,0

        st = []

        while i<len(pushed):
            st.append(pushed[i])

            while st and j<len(popped) and st[-1] == popped[j]:
                st.pop()
                j+=1

            i+=1
        
        return len(st) == 0