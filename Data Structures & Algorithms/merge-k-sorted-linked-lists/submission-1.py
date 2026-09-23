# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeTwoLists(list1, list2):
            dummy = head = ListNode()
            while list1 and list2:
                if list1.val<=list2.val:
                    head.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    head.next = ListNode(list2.val)
                    list2 = list2.next
                
                head = head.next

            if list1:
                head.next = list1
            if list2:
                head.next = list2

            return dummy.next
        

        listMain = ListNode()
        
        while len(lists)>1:
            mergedlists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1<len(lists) else None
                mergedlists.append(mergeTwoLists(list1, list2))

            lists = mergedlists

        print(lists)
        return lists[0] if lists else ListNode().next