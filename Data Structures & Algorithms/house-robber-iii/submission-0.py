# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def func(root):
            if not root:
                return (0,0)
            
            leftrob, leftdontrob= func(root.left)
            rightrob, rightdontrob = func(root.right)

            rob = root.val + leftdontrob + rightdontrob
            dont_rob = max(leftrob, leftdontrob)+ max(rightrob, rightdontrob)
            
            return (rob,dont_rob)
        
        rob, dont = func(root)
        return max(rob, dont)
        