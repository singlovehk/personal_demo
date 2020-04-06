# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        def helper(l1, l2, carry):
            if (l1 or l2 or carry):
                val1 = (l1.val if l1 else 0)
                val2 = (l2.val if l2 else 0)
                carry, digit = divmod(val1 + val2 + carry, 10)
                ans = ListNode(digit)
                ans.next = helper((l1.next if l1 else None), (l2.next if l2 else None), carry)
                return ans
            return None
        
        return helper(l1, l2, 0)
            
