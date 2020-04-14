# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes = {}
        def search(root, level):
            if root is None:
                nodes[level] = nodes.get(level, []) + ['None']
            else:
                nodes[level] = nodes.get(level, []) + [root.val]
                search(root.left, level+1)
                search(root.right, level+1)
        search(root, 0)
        for i in nodes:
            if nodes[i] != nodes[i][::-1]:
                return False
        return True
