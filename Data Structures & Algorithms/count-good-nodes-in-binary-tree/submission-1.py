# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
            
        ans = 0

        def check(root, key):
            nonlocal ans
            
            if not root:
                return None

            if root.val >= key:
                ans+=1
                key = root.val
            
            check(root.left, key)
            check(root.right, key)
        
        check(root, root.val)
        return ans