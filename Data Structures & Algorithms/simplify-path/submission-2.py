class Solution:
    def simplifyPath(self, path: str) -> str:
        
        arr = []
        st= []
        dir = ""
        for ch in path:
            if ch!="/":
                dir += ch
            else:
                if dir!="":
                    arr.append(dir)
                    dir = ""
        if dir!="":
            arr.append(dir)
        
        # print(arr)

        for dir in arr:
            # print(st, dir)
            if dir == ".":
                continue
            elif dir == "..":
                if st:
                    st.pop()
                continue
            st.append(dir)

        # print(st)
        
        if not st:
            return "/"
        return "/"+ "/".join(st)