# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def delete(root, key):

            if not root.left and not root.right:
                if root.val == key:
                    return None
                return root
            
            if key < root.val:
                root.left = delete(root.left, key)
            
            elif key > root.val:
                root.right = delete(root.right, key)
            
            else:
                if not root.left and not root.right:
                    return root
                
                elif root.left and not root.right:
                    return root.left
                
                elif root.right and not root.left:
                    return root.right
                else:
                    replacement = root.right

                    while replacement.left:
                        replacement = replacement.left
                    
                    root.val = replacement.val
                    root.right = delete(root.right, replacement.val)
            
            return root
        
        return delete(root,key)