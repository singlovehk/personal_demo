# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        final = ListNode(-1)
        pointer = final
        while l1 or l2:
            if l1 is None:
                head = ListNode(l2.val)
                l2 = l2.next
            elif l2 is None:
                head = ListNode(l1.val)
                l1 = l1.next
            elif l1.val<=l2.val:
                head = ListNode(l1.val)
                l1 = l1.next
            else:
                head = ListNode(l2.val)
                l2 = l2.next
            pointer.next = head
            pointer = head
        return final.next
