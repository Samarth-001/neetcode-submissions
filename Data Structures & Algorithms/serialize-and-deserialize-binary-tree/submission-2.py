class Codec:
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        st = ""

        def dfs(root):
            nonlocal st

            if not root:
                st += "N,"
                return

            st += str(root.val) + ","
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return st

        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        i = 0

        def dfs():
            nonlocal i

            if values[i] == "N":
                i += 1
                return None

            node = TreeNode(int(values[i]))
            i += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()