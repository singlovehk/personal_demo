# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def compare(p, q):
            if p is None and q is None:
                return True
            else:
                if q is None or p is None:
                    return False
                elif p.val != q.val:
                    return False
                else:
                    return (compare(p.left, q.left) and compare(p.right, q.right))
        return compare(p, q)
