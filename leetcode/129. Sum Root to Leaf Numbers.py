# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = []
        def helper(root, prev):
            if not root:
                pass
            elif not (root.left or root.right):
                queue.append(prev * 10 + root.val)
            else:
                helper(root.left, prev * 10 + root.val)
                helper(root.right, prev * 10 + root.val)
        helper(root, 0)
        return sum(queue)
