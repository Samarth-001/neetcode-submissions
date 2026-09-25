# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(root, lower_bound, upper_bound):
            if not root:
                return True
            
            # if not root.left and not root.right:
            #     return True

            if root.val<=lower_bound or root.val>=upper_bound:
                return False
        
            return valid(root.left, lower_bound, root.val) and valid(root.right, root.val, upper_bound)
        
        return valid(root, float("-inf"), float("inf"))