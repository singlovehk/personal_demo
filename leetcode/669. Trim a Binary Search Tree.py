# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def helper(root, L, R):
            if root is None:
                return None
            elif L<=root.val<=R:
                tree = TreeNode(root.val)
                tree.left = helper(root.left, L, R)
                tree.right = helper(root.right, L, R)
                return tree
            elif root.val>R:
                return helper(root.left, L, R)
            else:
                return helper(root.right, L, R)
            
        return helper(root, L, R)
