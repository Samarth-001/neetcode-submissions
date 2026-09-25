# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def remove(root):
            if not root:
                return None

            if not root.left and not root.right and root.val == target:
                return None           
            
            root.left = remove(root.left)
            root.right = remove(root.right)

            if not root.left and not root.right and root.val == target:
                return None

            return root
        
        return remove(root)
