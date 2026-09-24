# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def checkTree(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val!=q.val:
                return False

            return checkTree(p.left,q.left) and checkTree(p.right,q.right)

        return checkTree(p,q)