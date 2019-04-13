# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        node = head

        if not l1 and not l2: return None
        elif not l1:          return l2
        elif not l2:          return l1

        # move up
        mu = 0
        while l1 or l2:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            sum += mu
            mu = 0
            if sum >= 10:
                mu  = 1
                sum = sum - 10

            node.next = ListNode(sum)
            node = node.next
        
        if mu == 1:
            node.next = ListNode(1)

        return head.next