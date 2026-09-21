"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = dhead = Node(0)
        
        hm = {None: None}

        chead = head

        while chead:
            dhead.next = Node(chead.val)
            dhead = dhead.next
            hm[chead] = dhead
            chead = chead.next
        
        # print(hm)

        chead = head
        dhead = dummy.next

        # print(dhead.random)
        while chead:
            dhead.random = hm[chead.random]
            chead = chead.next
            dhead = dhead.next
        
        dummy = dummy.next

        return dummy