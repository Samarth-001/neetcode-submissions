# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def mdepth(root):
            if not root:
                return 0
            
            depth = 1 + max(mdepth(root.left), mdepth(root.right))

            return depth
        
        return mdepth(root)