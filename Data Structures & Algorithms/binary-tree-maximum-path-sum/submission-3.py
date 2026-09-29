# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxSum = float('-inf')

        def maxPath(root):
            nonlocal maxSum

            if not root:
                return 0
            
            left = maxPath(root.left)
            right = maxPath(root.right)

            left = max(0, left)
            right = max(0, right)


            temp = max(left+root.val,right+root.val)
            maxSum = max(maxSum, left+root.val+right)

            return temp
        
        maxPath(root)
        return maxSum