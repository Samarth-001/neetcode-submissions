# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
            
        queue = deque()
        queue.append(root)
        ans = []
        while len(queue)>0:
            level = 0
            iteration = len(queue)

            for _ in range(iteration):
                
                elpop = queue.popleft()
                level = elpop.val
                
                if elpop.left:
                    queue.append(elpop.left) 
                if elpop.right:
                    queue.append(elpop.right)

            ans.append(level)

        return ans 