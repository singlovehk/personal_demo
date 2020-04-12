# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = 0
        cur = head
        while cur:
            cur = cur.next
            i += 1
        cur = head
        for _ in range(i // 2):
            cur = cur.next
            
        return cur
