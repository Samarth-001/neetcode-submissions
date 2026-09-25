# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        curr = k
        ans = 0

        def inorder(root):
            nonlocal curr
            nonlocal ans

            if not root:
                return None
            
            inorder(root.left)
            curr-=1
            if curr==0:
                print(root.val, curr)
                ans = root.val
            inorder(root.right)
        
        inorder(root)
        return ans