# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        
        ans = l = ListNode(0)
        
        while l1 and l2:
            if l1.val <= l2.val: 
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            l = l.next
        if l1:
            l.next = l1
        if l2:
            l.next = l2
        
        return ans.next
        