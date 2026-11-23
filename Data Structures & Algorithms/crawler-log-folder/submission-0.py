class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        st = []

        for log in logs:
            if log[0:2] == "..":
                if not st:
                    continue
                st.pop()
            elif log[0:2] == "./":
                continue
            else:
                st.append(log)
        
        return len(st)