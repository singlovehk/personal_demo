# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        def helper(root):
            if root is None:
                return float('inf')
            elif not(root.left or root.right):
                return 1
            else:
                return min(helper(root.left) + 1, helper(root.right) + 1)
        return helper(root)
